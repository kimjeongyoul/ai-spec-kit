# 🛸 AI Spec-Kit: Spec-Driven AI Engineering

> **"코드를 짜지 마세요. 명세를 짜세요. 코드는 AI가 짭니다."**  
> AI 에이전트의 지능적 한계를 엔지니어링으로 제어하는 차세대 협업 표준

---

## 🚦 Series 1: 프로젝트 시작하기 (Quick Start)

`ai-spec-kit`을 프로젝트에 도입하고 기본 구조를 설정하는 단계입니다.

| # | 단계 | 명령어 | 설명 |
| :-- | :--- | :--- | :--- |
| 1 | **설치** | `uv tool install ...` | `uv`를 통한 글로벌 CLI 도구 설치 |
| 2 | **초기화** | `ai-spec init` | 표준 명세 구조(`specs/`) 및 AI 규칙(`rules.md`) 생성 |
| 3 | **환경 설정** | `.env` 세팅 | `.env.example`을 기반으로 API Key 보안 설정 |
| 4 | **동기화** | `ai-spec sync` | 수정된 명세와 AI 규칙을 실시간 동기화 |

---

## 🤖 Series 2: AI 에이전트 온보딩 (Collaboration)

AI와 인간이 같은 설계 도면을 공유하며 협업하는 과정입니다.

| # | 주제 | 핵심 내용 | 가이드라인 |
| :-- | :--- | :--- | :--- |
| 1 | **온보딩** | "명세를 먼저 읽어줘" | 첫 대화에서 AI에게 설계 철학 주입 |
| 2 | **행동 지침** | `.ai/rules.md` | AI가 매 답변마다 지켜야 할 필수 프로토콜 |
| 3 | **실시간 체크** | `status --brief` | 답변 끝에 붙는 한 줄의 건강 상태바 확인 |
| 4 | **구현 검증** | `ai-spec verify` | 작성된 코드가 명세를 이행했는지 추적성 검증 |

---

## 🛡️ Series 3: 엔지니어링 가드레일 (Guardrails)

AI가 무분별하게 코드를 짜지 않도록 방어적인 제약 조건을 설정합니다.

| # | 확장 옵션 | 명령어 플래그 | 효과 |
| :-- | :--- | :--- | :--- |
| 1 | **보안** | `--security` | OWASP Top 10 및 LLM 보안 가드레일 주입 |
| 2 | **웹 표준** | `--web` | 웹 접근성(WCAG) 및 SEO 최적화 명세 추가 |
| 3 | **라이선스** | `--license` | 오픈소스 라이선스 리스크(GPL 등) 원천 차단 |
| 4 | **운영 보호** | `Shield` | `APP_ENV=prod` 감지 시 모든 수정 작업 자동 차단 |

---

## ❄️ Series 4: 지능 상태 제어 (Context Management)

대화가 길어질 때 발생하는 AI의 지능 저하 문제를 엔지니어링으로 해결합니다.

| # | 기능 | 명령어 | 메커니즘 |
| :-- | :--- | :--- | :--- |
| 1 | **부하 측정** | `ai-spec status` | 현재 컨텍스트 사용량 및 지능 상태 수치화 |
| 2 | **지능 동결** | `ai-spec freeze` | 현재까지의 설계를 `context.md`로 직렬화(Freeze) |
| 3 | **기억 복구** | `ai-spec recover` | 세션 종료 또는 복구 시 체크포인트에서 지능 재주입 |
| 4 | **대안 추천** | `Optimization` | AI가 라이브러리 제안 시 2개 이상의 대안 비교 강제 |

---

## 🚀 Unique Insights (독보적 강점)

- **Spec-First Engineering**: 단순 가이드가 아닌 AI가 직접 읽고 행동하는 규칙을 자동 주입.
- **Context 1M Token Manager**: AI의 물리적 한계를 정량적으로 관리하고 제어.
- **Proactive Optimization**: AI가 더 나은 라이브러리를 고민하게 만드는 지능형 프로토콜.

---

*Created by [Jeongyoul Kim](https://github.com/kimjeongyoul)*
