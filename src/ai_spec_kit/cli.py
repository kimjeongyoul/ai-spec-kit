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
        json.dump(data, f, indent=2, ensure_ascii=False)

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

def check_production_shield():
    """운영 환경(Production)에서 실행되는 것을 방지하는 안전 장치"""
    shield_vars = ["APP_ENV", "PYTHON_ENV", "NODE_ENV", "STAGE", "ENV"]
    prod_indicators = ["PROD", "PRODUCTION", "RELEASE"]
    
    for var in shield_vars:
        val = os.getenv(var, "").upper()
        if any(ind in val for ind in prod_indicators):
            console.print(Panel(
                f"[bold red]🚫 PRODUCTION SHIELD ACTIVATED[/bold red]\n\n"
                f"현재 환경 변수 [bold yellow]{var}={os.getenv(var)}[/bold yellow]가 감지되었습니다.\n"
                "이 도구는 명세 중심의 '개발 및 설계' 전용 도구입니다.\n"
                "운영(Production) 환경에서의 실행은 코드 및 데이터 오염 위험이 있어 차단됩니다.\n\n"
                "[dim]실행이 꼭 필요하다면 환경 변수를 변경하거나 해제하세요.[/dim]",
                title="Safety Error", border_style="red"
            ))
            exit(1)

@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """[AI-Native Spec-Kit] AI 협업 및 지능 상태 관리 도구"""
    check_production_shield()
    
    if ctx.invoked_subcommand is None:
        console.print(Panel.fit(
            "[bold cyan]🚀 AI Spec-Kit CLI[/bold cyan]\n\n"
            "[bold yellow]1. SETUP[/bold yellow]\n"
            "   init      - 프로젝트 표준 구조 및 보안 세팅\n"
            "               [dim](옵션: --security, --web)[/dim]\n"
            "   sync      - 명세와 AI 규칙 동기화\n"
            "   recover   - 비정상 종료 시 지능 상태 복구\n\n"
            "[bold yellow]2. MONITORING[/bold yellow]\n"
            "   dashboard - AI 협업 건강 상태 확인\n"
            "   status    - 컨텍스트 부하 분석 및 자동 동결 제안\n\n"
            "[bold yellow]3. DEVELOPMENT[/bold yellow]\n"
            "   blueprint - 새 기능 명세서 생성\n"
            "   verify    - 구현 추적성 검증\n"
            "   freeze    - 현재 상태 요약 동결\n\n"
            "[bold dim]💡 Tip: 'ai-spec init --security --web'으로 모든 보안/웹 표준을 한 번에 세팅하세요![/bold dim]",
            title="Available Commands", border_style="cyan"
        ))

@main.command()
@click.argument('project_name', default=".")
@click.option('--security', is_flag=True, help="Include OWASP Security specification")
@click.option('--web', is_flag=True, help="Include Web Standards & Accessibility specifications")
def init(project_name, security, web):
    """표준 명세 구조 및 보안 인프라 초기화"""
    base_path = Path(project_name)
    spec_path = base_path / "specs"
    template_dir = Path(__file__).parent / "templates"
    os.makedirs(spec_path / "blueprints", exist_ok=True)
    os.makedirs(spec_path / "decisions", exist_ok=True)
    
    applied_specs = ["Core Architecture", "Engineering Standard", "AI Protocol"]
    
    # Core templates to copy and render
    core_templates = ["ai-protocol.md", "architecture.md", "engineering.md"]
    for t_name in core_templates:
        target_file = spec_path / t_name
        with open(template_dir / t_name, "r", encoding="utf-8") as f:
            content = f.read()
        rendered = Template(content).render(project_name=project_name if project_name != "." else "My Project")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(rendered)

    # Optional templates
    if security:
        shutil.copy(template_dir / "security.md", spec_path / "security.md")
        applied_specs.append("OWASP Security")
    if web:
        shutil.copy(template_dir / "accessibility.md", spec_path / "accessibility.md")
        shutil.copy(template_dir / "web-standards.md", spec_path / "web-standards.md")
        applied_specs.append("Web Accessibility & Standards")

    ai_path = base_path / ".ai"
    os.makedirs(ai_path, exist_ok=True)
    shutil.copy(template_dir / "ai-protocol.md", ai_path / "rules.md")
    
    with open(base_path / ".env.example", "w", encoding="utf-8") as f:
        f.write("GOOGLE_GENERATIVE_AI_API_KEY=your_key_here\nOPENAI_API_KEY=your_key_here\n")
    
    gitignore_path = base_path / ".gitignore"
    git_ignore_rules = [
        "\n# --- AI Spec-Kit ---",
        ".ai/checkpoint.json  # AI activity journal (Local only)",
        ".env                  # API Keys and Secrets",
        ".env.*",
        "!.env.example"
    ]
    
    existing_content = ""
    if gitignore_path.exists():
        with open(gitignore_path, "r", encoding="utf-8") as f:
            existing_content = f.read()
    
    with open(gitignore_path, "a", encoding="utf-8") as f:
        for rule in git_ignore_rules:
            clean_rule = rule.split('#')[0].strip()
            if not clean_rule or clean_rule not in existing_content:
                f.write(rule + "\n")
    
    save_checkpoint("INIT", f"Project {project_name} initialized")
    
    summary = "\n".join([f" - {s}" for s in applied_specs])
    console.print(Panel(
        f"[bold green]✅ 프로젝트 초기화 완료![/bold green]\n\n"
        f"[bold white]적용된 명세 목록:[/bold white]\n{summary}", 
        border_style="green"
    ))

    # 옵션 팁 출력
    if not (security and web and license):
        tips = "\n[bold yellow]💡 Tip: 아직 사용하지 않은 강력한 옵션들이 있습니다![/bold yellow]\n"
        if not security:
            tips += " - [bold cyan]--security[/bold cyan]: OWASP & LLM 보안 명세를 추가합니다.\n"
        if not web:
            tips += " - [bold cyan]--web[/bold cyan]: 웹 접근성 및 표준 명세를 추가합니다.\n"
        if not license:
            tips += " - [bold cyan]--license[/bold cyan]: 오픈소스 라이선스 정책 명세를 추가합니다.\n"
        console.print(tips)
    
    # AI Onboarding Guide
    onboarding_msg = (
        "\n[bold cyan]🤖 AI 에이전트와 대화를 시작할 때 아래 문구를 복사해서 붙여넣으세요:[/bold cyan]\n\n"
        "----------------------------------------------------------------------\n"
        "이 프로젝트는 `ai-spec-kit` 표준을 따르고 있어. 먼저 다음 파일들을 읽고 규칙을 숙지해줘:\n"
        "1. `.ai/rules.md` (너의 행동 지침이자 필수 보고 규칙이야)\n"
        "2. `specs/` 폴더의 모든 명세서들 (설계 방향이야)\n\n"
        "너는 매 답변 끝에 `ai-spec status --brief`를 실행하여 현재 상태를 보고해야 해.\n"
        "이 지침을 확인했다면 준비되었다고 말해줘.\n"
        "----------------------------------------------------------------------"
    )
    console.print(onboarding_msg)

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

def get_health_status():
    """프로젝트 건강 상태 체크 (Snap 및 Spec 상태)"""
    # 1. Snap (Checkpoint) Status
    checkpoint_path = Path(".ai/checkpoint.json")
    snap_status = "ERR"
    if checkpoint_path.exists():
        try:
            with open(checkpoint_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    snap_status = "OK"
        except: pass
    
    # 2. Spec Compliance (기본 명세 파일 존재 여부)
    required_specs = ["architecture.md", "engineering.md", "ai-protocol.md"]
    found_specs = 0
    for s in required_specs:
        if (Path("specs") / s).exists():
            found_specs += 1
    compliance_pct = int((found_specs / len(required_specs)) * 100)
    
    return snap_status, compliance_pct

@main.command()
@click.option('--brief', is_flag=True)
def status(brief):
    tokens, load_pct = get_context_stats()
    snap_status, compliance = get_health_status()
    
    if brief:
        # Traffic Light 스타일의 한 줄 상태바
        color = "green" if load_pct < 70 else "yellow" if load_pct < 90 else "red"
        console.print(f"[[bold {color}]AI Context: {load_pct:.1f}%[/bold {color}] | Snap: {snap_status} | Spec: {compliance}%]")
        return
    
    console.print(f"Estimated Tokens: {tokens:,} ({load_pct:.1f}%)")
    console.print(f"Checkpoint Status: [cyan]{snap_status}[/cyan]")
    console.print(f"Spec Compliance  : [cyan]{compliance}%[/cyan]")
    
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
anual freeze")
def freeze(reason):
    execute_freeze(reason)

if __name__ == "__main__":
    main()
