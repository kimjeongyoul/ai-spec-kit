# Engineering Standard Specification

## 🛠 Commit Convention (Spec-Driven)
모든 커밋은 작업의 성격과 대상 명세를 명확히 식별할 수 있어야 합니다.

### Format
`<type>(<scope>): <spec-id> - <description>`

### Types
- **feat**: 새로운 기능 명세 구현
- **spec**: 명세서(Blueprints/Architecture) 작성 및 수정
- **refactor**: 명세 변경 없이 코드 구조 개선
- **fix**: 명세와 불일치하는 버그 수정
- **docs**: 문서 수정

### Example
- `feat(auth): login-spec - implement JWT validation logic`
- `spec(api): payment-blueprint - define refund interface`
- `fix(core): architecture-spec - resolve context freezing logic error`

## 📐 Implementation Rule
- 모든 커밋은 하나의 명세 단위(Blueprint)를 넘지 않는 원자적(Atomic) 단위를 유지한다.
- 커밋 메시지만 보고도 어떤 명세 문서가 업데이트되었는지 추적 가능해야 한다.

## 🚫 Anti-Patterns (Never do this)
1. **Happy Path Bias**: 예외 처리(Error Handling)가 없는 코드는 구현되지 않은 것으로 간주한다.
2. **Library Bloat**: 새로운 패키지 추가 전 반드시 표준 라이브러리로 대체 가능한지 검토한다.
3. **Hard-coded Secrets**: 어떠한 경우에도 코드 내에 민감 정보(Key, PII)를 하드코딩하지 않는다.
4. **Silent Failure**: 에러를 catch하고 아무 작업도 하지 않는(Empty catch block) 행위를 금지한다.

## ✅ Definition of Done (DOD)
- [ ] 작업 내용이 관련 Blueprint 명세와 일치하는가?
- [ ] 주요 비즈니스 로직에 대한 유닛 테스트가 작성되었는가?
- [ ] 에러 핸들링 및 로그 메시지가 적절하게 포함되었는가?
- [ ] `ai-spec verify` 명령을 통해 추적성이 확인되었는가?

