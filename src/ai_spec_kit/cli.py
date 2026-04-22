import click
import os
import shutil
import subprocess
import json
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from jinja2 import Template

console = Console()

def save_checkpoint(activity_type, detail=""):
    """활동 내역을 .ai/checkpoint.json에 자동 저장 (방어적 메모리)"""
    checkpoint_path = Path(".ai/checkpoint.json")
    checkpoint_path.parent.mkdir(exist_ok=True)
    
    data = []
    if checkpoint_path.exists():
        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except: data = []

    data.append({
        "timestamp": datetime.now().isoformat(),
        "type": activity_type,
        "detail": detail
    })
    
    # 최근 20개만 유지 (Rolling Journal)
    data = data[-20:]
    
    with open(checkpoint_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ok=False)

def execute_freeze(reason):
    """실제 동결 로직을 수행하는 내부 함수"""
    path = Path("specs/context.md")
    content = f"# Project Context Freeze\n- Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n- Reason: {reason}\n\n## 📝 Status\n- AI Agent: Summary needed...\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    save_checkpoint("FREEZE", f"Context frozen to {path}")
    console.print(f"[bold blue]❄️ Context Frozen:[/bold blue] {path}")

def get_context_stats():
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
    """[AI-Native Spec-Kit] AI 협업 및 지능 상태 관리 도구"""
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit(
            "[bold cyan]🚀 AI Spec-Kit CLI[/bold cyan]\n\n"
            "[bold yellow]1. SETUP[/bold yellow]\n"
            "   init      - 프로젝트 표준 구조 및 보안 세팅\n"
            "   sync      - 명세와 AI 규칙 동기화\n"
            "   recover   - 비정상 종료 시 지능 상태 복구\n\n"
            "[bold yellow]2. MONITORING[/bold yellow]\n"
            "   dashboard - AI 협업 건강 상태 확인\n"
            "   status    - 컨텍스트 부하 분석 및 자동 동결 제안\n\n"
            "[bold yellow]3. DEVELOPMENT[/bold yellow]\n"
            "   blueprint - 새 기능 명세서 생성\n"
            "   verify    - 구현 추적성 검증\n"
            "   freeze    - 현재 상태 요약 동결\n",
            title="Available Commands", border_style="cyan"
        ))

@main.command()
@click.argument('project_name', default=".")
def init(project_name):
    """표준 명세 구조 및 보안 인프라 초기화"""
    base_path = Path(project_name)
    spec_path = base_path / "specs"
    template_dir = Path(__file__).parent / "templates"
    os.makedirs(spec_path / "blueprints", exist_ok=True)
    os.makedirs(spec_path / "decisions", exist_ok=True)
    
    for template_file in template_dir.glob("*.md"):
        target_file = spec_path / template_file.name
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        rendered = Template(content).render(project_name=project_name if project_name != "." else "My Project")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(rendered)

    ai_path = base_path / ".ai"
    os.makedirs(ai_path, exist_ok=True)
    shutil.copy(template_dir / "ai-protocol.md", ai_path / "rules.md")
    
    with open(base_path / ".env.example", "w", encoding="utf-8") as f:
        f.write("GOOGLE_GENERATIVE_AI_API_KEY=your_key_here\nOPENAI_API_KEY=your_key_here\n")
    
    with open(base_path / ".gitignore", "a", encoding="utf-8") as f:
        f.write("\n.env\n.env.*\n.ai/checkpoint.json\n")
    
    save_checkpoint("INIT", f"Project {project_name} initialized")
    console.print("[bold green]✅ 프로젝트 초기화 및 보안 세팅 완료![/bold green]")

@main.command()
def recover():
    """비정상 종료된 세션의 마지막 활동 기록을 기반으로 상태를 복구합니다."""
    checkpoint_path = Path(".ai/checkpoint.json")
    if not checkpoint_path.exists():
        console.print("[bold red]❌ 복구할 체크포인트 기록이 없습니다.[/bold red]")
        return

    with open(checkpoint_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    console.print(Panel.fit("[bold yellow]🛠 AI Memory Recovery[/bold yellow]\n\n최근 활동을 기반으로 상태를 복구합니다."))
    for entry in data[-5:]:
        console.print(f"[dim]{entry['timestamp']}[/dim] | [cyan]{entry['type']}[/cyan] - {entry['detail']}")

    if click.confirm("\n이 기록들을 바탕으로 'specs/context.md'를 강제 생성할까요?"):
        path = Path("specs/context.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Recovered Context ({datetime.now().strftime('%Y-%m-%d')})\n\n## Recent Activities\n")
            for entry in data[-10:]:
                f.write(f"- {entry['timestamp']}: {entry['type']} ({entry['detail']})\n")
        console.print(f"[bold green]✅ 복구 완료: {path}[/bold green]")

@main.command()
def verify():
    """명세 구현 정합성 검증"""
    save_checkpoint("VERIFY", "Compliance check performed")
    # ... (기존 verify 로직) ...
    blueprints = [f.stem for f in Path("specs/blueprints").glob("*.md")]
    table = Table(title="Implementation Traceability")
    table.add_column("Spec ID", style="magenta")
    table.add_column("Status", justify="center")
    for bp in blueprints:
        has_commit = False
        try:
            subprocess.check_output(["git", "log", "--grep", bp, "-n", "1"], stderr=subprocess.STDOUT)
            has_commit = True
        except: pass
        table.add_row(bp, "[green]YES[/green]" if has_commit else "[yellow]NO[/yellow]")
    console.print(table)

@main.command()
@click.argument('name')
def blueprint(name):
    """새 명세서 생성"""
    path = Path("specs/blueprints") / f"{name}.md"
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Blueprint: {name}\n")
    save_checkpoint("BLUEPRINT", f"Created spec: {name}")
    console.print(f"[bold green]✨ 생성됨: {path}[/bold green]")

@main.command()
@click.option('--brief', is_flag=True)
def status(brief):
    tokens, load_pct = get_context_stats()
    if brief:
        console.print(f"[AI Context: {load_pct:.1f}%]")
        return
    console.print(f"Estimated Tokens: {tokens:,} ({load_pct:.1f}%)")
    if load_pct >= 80 and click.confirm("Freeze now?"):
        execute_freeze("Auto-freeze")

@main.command()
def sync():
    shutil.copy("specs/ai-agent-protocol.md", ".ai/rules.md")
    save_checkpoint("SYNC", "AI Rules synchronized")
    console.print("[green]🔄 Sync Complete[/green]")

@main.command()
@click.option('--reason', default="Manual freeze")
def freeze(reason):
    execute_freeze(reason)

if __name__ == "__main__":
    main()
