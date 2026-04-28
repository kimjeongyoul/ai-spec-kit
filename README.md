# 🚀 AI Spec-Kit

**AI-Native Specification-Driven Development (SDD) Standard**

`ai-spec-kit`은 AI 에이전트(Gemini, Claude, Copilot 등)와의 협업에서 발생하는 '맥락 상실'과 '설계 이탈'을 방지하기 위한 명세 중심 개발 표준화 도구입니다. 감에 의존하는 프롬프팅(Vibe Coding)을 넘어, 구조화된 명세를 통해 AI가 일관성 있게 코딩하도록 가이드합니다.

---

## 📦 설치 (Installation)

`uv`를 사용하여 최신 버전을 설치하는 것을 권장합니다.

```bash
# 최신 버전 설치 및 업데이트
uv tool install ai-spec-kit --from git+https://github.com/kimjeongyoul/ai-spec-kit.git --force
```

---

## 🛠 주요 기능 (Key Commands)

### 1. 프로젝트 초기화 (`init`)
프로젝트 성격에 맞는 표준 명세 구조와 AI 에이전트용 규칙 파일을 생성합니다.
```bash
ai-spec init --security --web --license
```
- `--security`: OWASP 및 LLM 보안 가이드라인 포함
- `--web`: 웹 표준 및 접근성 가이드라인 포함
- `--license`: 오픈소스 라이선스 준수 정책 포함

### 2. 최신 표준 업데이트 (`update`) ✨ NEW
프로젝트 진행 중에도 `ai-spec-kit`의 최신 템플릿과 보안 규칙을 반영할 수 있습니다. 기존 커스터마이징을 보호하기 위해 파일별 덮어쓰기 확인을 거칩니다.
```bash
ai-spec update --security --web --license
```

### 3. 상태 모니터링 (`status`)
현재 AI 에이전트가 참고하는 컨텍스트 부하와 명세 준수율을 확인합니다.
```bash
ai-spec status
# 혹은 한 줄 요약 보고 (AI 에이전트 답변 끝에 붙이기 용도)
ai-spec status --brief
```

### 4. 지능 상태 동결 (`freeze`)
AI가 지금까지의 대화 맥락과 결정 사항을 잊지 않도록 `specs/context.md`에 현재 상태를 요약하여 박제합니다.
```bash
ai-spec freeze --reason "v1.0 기능 구현 완료"
```

### 5. 명세 구현 검증 (`verify`)
작성된 기능 명세(Blueprint)가 실제 코드로 구현되어 Git 히스토리에 반영되었는지 추적합니다.
```bash
ai-spec verify
```

---

## 🔄 AI 에이전트와 협업하는 방법

1. **Setup:** `ai-spec init`으로 구조 잡기.
2. **Specify:** `ai-spec blueprint <name>`으로 새 기능 정의.
3. **Prompt:** AI에게 `.ai/rules.md`와 `specs/`의 명세를 먼저 읽으라고 지시.
4. **Monitor:** AI가 작업 완료 시 `ai-spec status --brief`를 출력하게 하여 프로젝트 건강 상태 공유.
5. **Freeze:** 중요한 결정이 내려지면 `ai-spec freeze`로 맥락 고정.

---

## 🛡️ 안전 가드레일 (Production Shield)

이 도구는 **설계 및 개발 전용**입니다. 실수로 운영(Production) 환경에서 실행되어 설계 파일이 오염되는 것을 방지하기 위해 `APP_ENV=production` 등의 환경 변수가 감지되면 실행이 자동으로 차단됩니다.

---

## 🏛 Why `ai-spec-kit`?

- **Anti-Hallucination:** 명세라는 명확한 기준을 제공하여 AI의 환각 증상을 줄입니다.
- **Context Management:** 무의미하게 길어지는 컨텍스트를 동결(Freeze)하여 토큰을 절약하고 지능을 유지합니다.
- **Traceability:** 설계와 구현 사이의 연결 고리를 유지합니다.

---

**도움이 되셨다면 ⭐️ Star를 눌러 응원해주세요!** 121명의 초기 사용자분들의 피드백은 언제나 환영합니다.
