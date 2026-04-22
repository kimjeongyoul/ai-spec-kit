# AI Spec-Kit

**AI 에이전트의 지능적 한계를 엔지니어링으로 제어하는 명세 중심 개발 표준**

GitHub의 `spec-kit` 철학을 계승하되, **AI 에이전트 협업 환경**에 최적화된 고유한 가치를 제공합니다.

## 🚀 설치 및 실행 (Quick Installation)

`uv`가 설치되어 있다면 아래 한 줄로 즉시 전역 도구로 설치하고 사용할 수 있습니다.

```bash
uv tool install ai-spec-kit --from git+https://github.com/kimjeongyoul/ai-spec-kit.git
```

---

## 🤖 AI 에이전트와 시작하기 (Onboarding Guide)

`ai-spec init`으로 프로젝트를 초기화했다면, 사용 중인 AI 에이전트(Gemini, Claude 등)에게 첫 대화로 다음과 같이 지시하세요.

> **"이 프로젝트는 `ai-spec-kit` 표준을 따르고 있어. `.ai/rules.md` 파일을 읽고 내 협업 규칙을 숙지해줘. 그리고 `specs/` 폴더의 명세서들을 분석한 뒤에 개발을 시작하자."**

이 한마디로 AI는 사용자님의 설계 철학과 컨텍스트 관리 룰을 즉시 학습하게 됩니다.

---

## 🛠 주요 명령어

### 1. 프로젝트 초기화
```bash
ai-spec init
```
- 표준 명세 구조(`specs/`) 생성 및 AI 행동 지침(`.ai/rules.md`) 주입.

### 2. 컨텍스트 및 건강 상태 확인
```bash
ai-spec dashboard
```
- 컨텍스트 부하, 명세 이행률 등을 한눈에 확인하는 종합 상황판.

### 3. 실시간 컨텍스트 모니터링
```bash
ai-spec status --brief
```
- AI 답변 끝에 붙이기 좋은 한 줄 상태바 출력. (AI에게 매 답변마다 이 명령을 실행하도록 시키세요!)

### 4. 명세 기반 구현 검증
```bash
ai-spec verify
```
- 설계 명세와 실제 커밋 로그/파일 구조를 대조하여 정합성 체크.

### 5. 최신 표준 업데이트
```bash
# 1. 도구 자체 업데이트
uv tool install ai-spec-kit --from git+https://github.com/kimjeongyoul/ai-spec-kit.git --force

# 2. 프로젝트 내 템플릿 및 규칙 업데이트
ai-spec update
```

---

## 🛡️ 안전한 업데이트 및 커스터마이징 가이드

`ai-spec update`는 기존에 진행 중인 프로젝트의 소중한 설계를 보호하기 위해 다음과 같이 작동합니다.

### 1. 선택적 덮어쓰기 (Selective Overwrite)
- `specs/architecture.md` 등 기존 파일이 이미 존재할 경우, 도구는 덮어쓸지 여부를 **파일마다 개별적으로** 물어봅니다.
- 본인만의 커스터마이징이 많이 반영된 파일이라면 `n`을 선택하여 현재 상태를 유지하세요.

### 2. 사용자 데이터 보호 영역
- 사용자가 생성한 개별 기능 명세(`specs/blueprints/*.md`)와 의사결정 기록(`specs/decisions/*.md`)은 **업데이트 대상에서 제외**되어 안전하게 보존됩니다.

### 3. 추천 워크플로우 (Git 활용)
- 업데이트를 실행하기 전, 현재의 작업물을 **Commit** 해두는 것을 권장합니다.
- 업데이트 후 `git diff`를 통해 표준 템플릿의 어떤 내용(예: 새로운 보안 규칙, AI 빌드 룰 등)이 추가되었는지 확인하고, 본인의 커스터마이징 내용과 적절히 병합(Merge)하세요.

---

## 🏛 Why `ai-spec-kit`? (Comparison)

| 비교 항목 | GitHub `spec-kit` | **ai-spec-kit (Ours)** |
| :--- | :--- | :--- |
| **협업 대상** | 사람(개발자) 간의 협업 | **사람과 AI 에이전트** 간의 협업 |
| **핵심 문제** | "문서가 없어서 개발이꼬인다" | **"AI가 컨텍스트를 잊거나 명세를 무시한다"** |
| **핵심 강점** | 보편적인 설계 표준화 | **AI의 지능적 한계(Context)를 엔지니어링으로 제어** |

---

## 🚀 독보적 인사이트 (Unique Insights)

1.  **AI의 물리적 한계 제어 (The 1M Token Manager)**: `status` 명령을 통해 AI의 기억력 부하를 정량적으로 측정하고 관리합니다.
2.  **실행 가능한 행동 지침**: 단순 가이드가 아닌 AI가 직접 읽고 행동하는 규칙(`.ai/rules.md`)을 자동으로 프로젝트에 주입합니다.
3.  **AI Memory Serialization**: 대화가 길어질 때 지능 상태를 파일로 직렬화하여 기억을 보존하는 **Freeze & Restore** 기술을 제시합니다.

---
*Created by [Jeongyoul Kim](https://github.com/kimjeongyoul)*
