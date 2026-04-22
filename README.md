# AI Spec-Kit

**AI 에이전트의 지능적 한계를 엔지니어링으로 제어하는 명세 중심 개발 표준**

GitHub의 `spec-kit` 철학을 계승하되, **AI 에이전트 협업 환경**에 최적화된 고유한 기능을 제공합니다.

## 🚀 왜 이 도구가 필요한가요? (Originality)
단순한 문서화를 넘어, AI 에이전트와 긴 호흡으로 협업할 때 발생하는 치명적인 문제들을 해결합니다.

1.  **AI 컨텍스트 윈도우 관리 (The 1M Token Manager)**: 
    - AI의 기억력 부하를 정량적으로 분석(`ai-spec status`)하여, 모델이 멍청해지기 전에 미리 대응할 수 있게 돕습니다.
2.  **행동 지침 자동 주입**: 
    - AI가 직접 읽고 스스로를 통제하게 만드는 실행 가능한 규칙(`.cursor/rules.md`)을 프로젝트에 즉시 주입합니다.
3.  **지능 상태 동결 및 복구 (Freeze & Resume)**: 
    - 대화가 길어져 AI가 이전 결정을 잊을 때, 현재의 프로젝트 지능 상태를 `context.md`로 직렬화하여 다음 세션으로 안전하게 전달합니다.

## 🛠 주요 명령어

### 1. 프로젝트 초기화
```bash
ai-spec init
```
- 표준 명세 구조(`specs/`) 생성 및 AI 행동 지침(`.cursor/rules.md`) 주입.

### 2. 컨텍스트 부하 분석
```bash
ai-spec status
```
- 현재 프로젝트의 파일 크기를 분석하여 AI의 예상 토큰 점유율 시각화.

### 3. 명세 기반 구현 검증
```bash
ai-spec verify
```
- `specs/blueprints`의 명세 목록과 Git 커밋 로그를 대조하여 구현 누락 여부 체크.

### 4. 컨텍스트 동결
```bash
ai-spec freeze --reason "feature-complete"
```
- 현재 지능 상태를 `specs/context.md`로 요약 저장하여 새 세션 준비.

## 🌟 철학
"명세가 구현을 이끌고, 데이터가 AI를 통제한다." 
이 도구는 개발자가 설계에 집중하게 하고, AI가 그 설계를 완벽히 수행하도록 보조하는 **AI-Native 엔지니어링의 인프라**입니다.

---
*Created by [Jeongyoul Kim](https://github.com/kimjeongyoul)*
