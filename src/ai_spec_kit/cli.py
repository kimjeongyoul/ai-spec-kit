import click
import os
import shutil
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from jinja2 import Template

console = Console()

@click.group()
def main():
    """
    [AI-Native Spec-Kit]
    명세(Specification)가 구현(Implementation)을 이끄는 개발 표준 도구입니다.
    """
    pass

@main.command()
@click.argument('project_name', default=".")
def init(project_name):
    """표준 명세 구조 및 AI 협업 프로토콜을 초기화합니다."""
    base_path = Path(project_name)
    spec_path = base_path / "specs"
    template_dir = Path(__file__).parent / "templates"

    console.print(Panel.fit(f"[bold cyan]🏛 Spec-Kit 표준화 프로세스 시작[/bold cyan]\nTarget: {base_path.absolute()}", border_style="cyan"))

    os.makedirs(spec_path / "blueprints", exist_ok=True)
    os.makedirs(spec_path / "decisions", exist_ok=True)
    
    for template_file in template_dir.glob("*.md"):
        target_file = spec_path / template_file.name
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        rendered = Template(content).render(project_name=project_name if project_name != "." else "My Project")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(rendered)
        console.print(f"  [green]✔[/green] 명세 템플릿 생성: {target_file.name}")

    cursor_path = base_path / ".cursor"
    os.makedirs(cursor_path, exist_ok=True)
    shutil.copy(template_dir / "ai-protocol.md", cursor_path / "rules.md")
    console.print(f"  [green]✔[/green] AI Agent 규칙 주입: .cursor/rules.md")
    console.print("\n[bold green]✅ 초기화 완료! 명세를 먼저 작성하고 AI와 협업하세요.[/bold green]")

@main.command()
def status():
    """현재 프로젝트의 AI 컨텍스트 부하 상태를 분석합니다."""
    console.print("[bold cyan]🔍 AI Context Load Analysis[/bold cyan]\n")
    total_size = 0
    exclude = {'.git', 'node_modules', '__pycache__', 'dist', 'build', '.next'}
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            if f.endswith(('.md', '.ts', '.tsx', '.py', '.java', '.json')):
                total_size += os.path.getsize(os.path.join(root, f))
    
    est_tokens = total_size // 3 
    load_pct = min((est_tokens / 1000000) * 100, 100)
    console.print(f"- **Estimated Tokens**: {est_tokens:,} / 1,000,000 ({load_pct:.1f}%)")
    if load_pct > 80:
        console.print("[bold red]⚠ 경고: 컨텍스트가 너무 무겁습니다. 'ai-spec freeze'를 실행하세요.[/bold red]")

@main.command()
def verify():
    """명세와 구현의 정합성을 검증합니다 (커밋 추적성 체크)."""
    console.print("[bold cyan]🛡 Spec-Kit Compliance Verification[/bold cyan]\n")
    
    # 1. Blueprint 추적성 체크
    blueprints = [f.stem for f in Path("specs/blueprints").glob("*.md")]
    table = Table(title="Blueprint Traceability")
    table.add_column("Specification", style="magenta")
    table.add_column("Status", justify="center")
    table.add_column("Last Commit", style="green")

    for bp in blueprints:
        try:
            # 커밋 메시지에서 해당 명세 ID가 포함되어 있는지 확인
            log = subprocess.check_output(
                ["git", "log", "--grep", bp, "-n", "1", "--oneline"],
                stderr=subprocess.STDOUT
            ).decode('utf-8').strip()
            
            if log:
                table.add_row(bp, "[green]Implemented[/green]", log[:50] + "...")
            else:
                table.add_row(bp, "[yellow]Pending[/yellow]", "No linked commit found")
        except:
            table.add_row(bp, "[red]Error[/red]", "Git not initialized or error")

    console.print(table)
    
    # 2. Context Freshness 체크
    ctx_file = Path("specs/context.md")
    if ctx_file.exists():
        mtime = os.path.getmtime(ctx_file)
        # 마지막 수정 이후 깃 변경사항이 있는지 간접 체크 (단순 예시)
        console.print(f"\n[dim]- Last Context Freeze: {ctx_file.name} exists.[/dim]")
    else:
        console.print("\n[bold red]✖ specs/context.md가 없습니다. 대화 요약 관리가 필요합니다.[/bold red]")

@main.command()
@click.option('--reason', default="Manual freeze", help="동결 사유")
def freeze(reason):
    """현재까지의 진행 상황을 요약하여 specs/context.md로 동결합니다."""
    path = Path("specs/context.md")
    content = f"# Project Context Freeze\n- Reason: {reason}\n\n## 📝 Status\n- AI Agent: Summary needed...\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    console.print(f"[bold blue]❄️ Context Frozen:[/bold blue] {path}")

@main.command()
@click.argument('name')
def blueprint(name):
    """새로운 기능 명세서(Blueprint)를 생성합니다."""
    path = Path("specs/blueprints") / f"{name}.md"
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Blueprint: {name}\n\n## 📋 Requirements\n\n## 📐 Interface Specification\n")
    console.print(f"[bold green]✨ 새 명세서 생성됨: {path}[/bold green]")

if __name__ == "__main__":
    main()
