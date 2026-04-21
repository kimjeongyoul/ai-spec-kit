# Architecture Specification: {{ project_name }}

## 1. System Overview
[이 시스템이 해결하려는 근본적인 비즈니스 문제와 핵심 가치를 기술하세요.]

## 2. Technical Stack & Rationale
- **Frontend**: [e.g., Next.js 14 (App Router)] - [선택 이유: 성능, SEO, 개발 생산성 등]
- **AI Integration**: [e.g., Vercel AI SDK] - [선택 이유: 멀티 LLM 지원 및 스트리밍 최적화]
- **Tooling Interface**: [e.g., MCP (Model Context Protocol)] - [선택 이유: 도구의 재사용성 및 표준화]

## 3. Layered Architecture
- **Consumer Layer**: 사용자 인터페이스 및 상호작용
- **Orchestration Layer**: LLM 추론 및 도구 실행 제어
- **Resource Layer**: 비즈니스 로직 및 외부 데이터 연동 (MCP Servers)

## 4. Key Decisions (ADR)
- [중요한 아키텍처 결정 사항을 기록하세요. 예: 왜 전역 상태 관리 대신 캐시 라이브러리를 썼는가?]
