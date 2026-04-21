import click
import os
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from jinja2 import Template

console = Console()

@click.group()
def main():
    """
    [AI-Native Spec-Kit]
    AI 에이전트와의 협업을 위한 명세 중심 개발 표준 도구입니다.
    """
    pass

@main.command()
@click.argument('project_name', default=".")
def init(project_name):
    """표준 명세 구조(specs/) 및 AI 협업 프로토콜을 초기화합니다."""
    base_path = Path(project_name)
    spec_path = base_path / "specs"
    template_dir = Path(__file__).parent / "templates"

    console.print(Panel.fit(f"[bold cyan]🏛 Spec-Kit 표준화 프로세스 시작[/bold cyan]\nTarget: {base_path.absolute()}", border_style="cyan"))

    # 1. 디렉토리 구조 생성
    os.makedirs(spec_path / "blueprints", exist_ok=True)
    os.makedirs(spec_path / "decisions", exist_ok=True)
    
    # 2. 템플릿 렌더링 및 복사
    for template_file in template_dir.glob("*.md"):
        target_file = spec_path / template_file.name
        
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Architecture 명세 등에 프로젝트 이름 주입
        rendered = Template(content).render(project_name=project_name if project_name != "." else "My Project")
        
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(rendered)
        
        console.print(f"  [green]✔[/green] 명세 템플릿 생성 완료: {target_file.name}")

    # 3. .cursor/rules 주입 (필수 협업 룰)
    cursor_path = base_path / ".cursor"
    os.makedirs(cursor_path, exist_ok=True)
    shutil.copy(template_dir / "ai-protocol.md", cursor_path / "rules.md")
    console.print(f"  [green]✔[/green] AI Agent 규칙 주입 완료: .cursor/rules.md")

    console.print("\n[bold green]✅ 이제 명세를 먼저 작성하고 AI와 대화를 시작하세요![/bold green]")

@main.command()
@click.argument('name')
def blueprint(name):
    """새로운 기능 명세서(Blueprint)를 생성합니다."""
    path = Path("specs/blueprints") / f"{name}.md"
    if not path.parent.exists():
        console.print("[bold red]❌ specs/ 구조가 없습니다. 'ai-spec init'을 먼저 실행하세요.[/bold red]")
        return

    content = f"# Blueprint: {name}\n\n## 📋 Requirements\n\n## 📐 Interface Specification\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    console.print(f"[bold green]✨ 새 기능 명세서가 생성되었습니다: {path}[/bold green]")

if __name__ == "__main__":
    main()
