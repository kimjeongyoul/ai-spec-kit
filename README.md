# AI Spec-Kit

**명세(Specification)가 구현(Implementation)을 이끄는 AI-Native 개발 표준 도구**

## 💡 Philosophy
단순히 코드를 양산하는 시대를 넘어, AI가 개발자의 설계 의도를 완벽히 이해하고 협업하는 것이 중요해졌습니다. `ai-spec-kit`은 **Model Context Protocol (MCP)**과 **Specification-Driven Development**의 철학을 결합하여, 어떤 프로젝트에서도 일관된 고품질의 아키텍처를 유지하게 돕습니다.

## 🌟 Key Features
- **Spec-Driven Initializer**: `specs/` 폴더 내에 아키텍처, ADR(Decision Records), 블루프린트 템플릿을 표준화된 양식으로 제공합니다.
- **AI Agent Protocol**: 컨텍스트 1M 토큰 모니터링 및 `context.md` 동결(Freeze) 로직이 포함된 행동 지침을 자동 주입합니다.
- **SSOT Management**: 구현 전 명세 합의를 강제하여 AI의 환각(Hallucination)을 줄이고 추론 품질을 높입니다.

## 🚀 Quick Start
```bash
# 설치
uv tool install ai-spec-kit --from git+https://github.com/kimjeongyoul/ai-spec-kit.git

# 프로젝트 초기화
ai-spec init my-project

# 새로운 기능 명세 생성
ai-spec blueprint feature-name
```

## 🏗 Architecture
- **`.cursor/rules.md`**: 에이전트의 자기 통제 및 컨텍스트 관리 룰.
- **`specs/architecture.md`**: 기술 스택의 합리적 근거(Rationale)와 계층 구조 명세.
- **`specs/decisions/`**: 아키텍처 결정 사항(ADR) 기록 보관소.

---
*본 도구는 단순한 템플릿 생성기가 아닌, 개발자와 AI가 같은 설계도를 공유하게 만드는 **협업 인프라**입니다.*
