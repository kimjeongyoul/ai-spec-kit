import click
import os
import shutil
import subprocess
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from jinja2 import Template

console = Console()

def execute_freeze(reason):
    """실제 동결 로직을 수행하는 내부 함수"""
    path = Path("specs/context.md")
    content = f"# Project Context Freeze\n- Reason: {reason}\n\n## 📝 Status\n- AI Agent: Summary needed...\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    console.print(f"[bold blue]❄️ Context Frozen:[/bold blue] {path}")

def get_context_stats():
    """컨텍스트 부하 통계를 계산하여 반환"""
    total_size = 0
    exclude = {'.git', 'node_modules', '__pycache__', 'dist', 'build', '.next'}
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            if f.endswith(('.md', '.ts', '.tsx', '.py', '.java', '.json')):
                total_size += os.path.getsize(os.path.join(root, f))
    est_tokens = total_size // 3 
    return est_tokens, min((est_tokens / 1000000) * 100, 100)

@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """
    [AI-Native Spec-Kit]
    AI 에이전트와의 협업을 위한 명세 중심 개발 표준 도구입니다.
    """
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit(
            "[bold cyan]🚀 AI Spec-Kit CLI[/bold cyan]\n\n"
            "[bold yellow]1. SETUP[/bold yellow]\n"
            "   init      - 프로젝트 표준 명세 구조 초기화\n"
            "   sync      - 명세와 AI 지침(.ai/rules.md) 동기화\n\n"
            "[bold yellow]2. MONITORING[/bold yellow]\n"
            "   dashboard - 프로젝트 건강 상태 종합 상황판\n"
            "   status    - AI 컨텍스트 부하 분석 및 동결 제안\n\n"
            "[bold yellow]3. DEVELOPMENT[/bold yellow]\n"
            "   blueprint - 새로운 기능 명세서 생성\n"
            "   verify    - 명세-구현 정합성 검증\n"
            "   freeze    - 현재 상태 요약 및 동결\n\n"
            "[dim]명령어 상세 정보는 'ai-spec [command] --help'를 입력하세요.[/dim]",
            title="Available Commands",
            border_style="cyan"
        ))

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

    # .ai 폴더로 규칙 주입
    ai_path = base_path / ".ai"
    os.makedirs(ai_path, exist_ok=True)
    shutil.copy(template_dir / "ai-protocol.md", ai_path / "rules.md")
    console.print(f"  [green]✔[/green] AI Agent 규칙 주입: .ai/rules.md")
    console.print("\n[bold green]✅ 초기화 완료! 'ai-spec dashboard'로 시작하세요.[/bold green]")

@main.command()
def dashboard():
    """프로젝트의 AI 협업 준비 상태를 종합적으로 보여줍니다."""
    console.print(Panel.fit("[bold cyan]📊 AI-Native Project Dashboard[/bold cyan]", border_style="cyan"))
    
    # 1. 컨텍스트 상태
    tokens, pct = get_context_stats()
    color = "red" if pct > 80 else "yellow" if pct > 50 else "green"
    console.print(f"\n[bold]1. AI Context Window[/bold]")
    console.print(f"   Load: [{color}]{pct:.1f}%[/{color}] ({tokens:,} / 1,000,000 tokens)")
    
    # 2. 명세 이행 상태
    blueprints = list(Path("specs/blueprints").glob("*.md"))
    console.print(f"\n[bold]2. Specification Status[/bold]")
    console.print(f"   Blueprints: {len(blueprints)} defined")
    
    ctx_file = Path("specs/context.md")
    ctx_status = "[green]Fresh[/green]" if ctx_file.exists() else "[red]Missing[/red]"
    console.print(f"   Memory Snapshot: {ctx_status}")
    
    console.print(f"\n[dim]팁: 'ai-spec verify'를 입력하면 상세 이행 내역을 확인합니다.[/dim]")

@main.command()
@click.option('--brief', is_flag=True, help="최소 정보만 한 줄로 출력합니다.")
def status(brief):
    """현재 프로젝트의 AI 컨텍스트 부하 상태를 분석하고 동결을 제안합니다."""
    tokens, load_pct = get_context_stats()
    
    if brief:
        # AI가 답변 끝에 붙이기 좋은 초간략 버전
        ctx_file = Path("specs/context.md")
        snap = "OK" if ctx_file.exists() else "MISSING"
        console.print(f"[AI Context: {load_pct:.1f}% | Snap: {snap}]")
        return

    console.print(f"[bold cyan]🔍 AI Context Load Analysis[/bold cyan]")
    console.print(f"- **Estimated Tokens**: {tokens:,} / 1,000,000 ({load_pct:.1f}%)")
    
    if load_pct >= 80:
        console.print(f"[bold red]⚠ 경고: 컨텍스트 부하가 임계점에 도달했습니다![/bold red]")
        if click.confirm("\n지금 바로 진행 상황을 요약하여 'specs/context.md'로 동결(Freeze)할까요?"):
            execute_freeze("Automated freeze via status check")
    else:
        console.print("[bold green]✅ 현재 AI가 쾌적하게 추론할 수 있는 상태입니다.[/bold green]")

@main.command()
def sync():
    """명세서의 변경 사항을 AI 에이전트 행동 지침(.ai/rules.md)에 동기화합니다."""
    protocol_spec = Path("specs/ai-agent-protocol.md")
    ai_rules = Path(".ai/rules.md")
    
    if not protocol_spec.exists():
        console.print("[bold red]❌ specs/ai-agent-protocol.md 파일이 없습니다.[/bold red]")
        return
        
    shutil.copy(protocol_spec, ai_rules)
    console.print("[bold green]🔄 AI Agent 행동 지침 동기화 완료! (.ai/rules.md)[/bold green]")

@main.command()
def verify():
    """명세와 구현의 정합성을 검증합니다 (커밋 및 파일 체크)."""
    console.print("[bold cyan]🛡 Spec-Kit Compliance Verification[/bold cyan]\n")
    
    blueprints = [f.stem for f in Path("specs/blueprints").glob("*.md")]
    table = Table(title="Implementation Traceability")
    table.add_column("Spec ID", style="magenta")
    table.add_column("Commit", justify="center")
    table.add_column("File Existence", justify="center")

    for bp in blueprints:
        # 1. 커밋 체크
        has_commit = False
        try:
            subprocess.check_output(["git", "log", "--grep", bp, "-n", "1"], stderr=subprocess.STDOUT)
            has_commit = True
        except: pass
        
        # 2. 파일 존재 여부 체크 (간이 검색)
        has_file = any(Path(".").rglob(f"*{bp}*"))
        
        table.add_row(
            bp, 
            "[green]YES[/green]" if has_commit else "[yellow]NO[/yellow]",
            "[green]FOUND[/green]" if has_file else "[dim]NOT FOUND[/dim]"
        )

    console.print(table)

@main.command()
@click.option('--reason', default="Manual freeze", help="동결 사유")
def freeze(reason):
    """현재까지의 진행 상황을 요약하여 specs/context.md로 동결합니다."""
    execute_freeze(reason)

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
