---
name: ios-architecture
description: 
  SwiftUI project structure guidance. Use when creating new projects, new features, new screens, file placement, file naming, folder organization, code refactoring, ViewModel separation, standard directory structure, MVVM. Follows user intent rather than enforcing specific architectural patterns.
allowed-tools: Read, Grep, Glob, Bash
---

<!-- APPSPEC-PRELUDE -->

> **ĐỌC KHỐI NÀY TRƯỚC.** File này lấy nguyên văn từ bộ **app-spec** rồi đưa vào Pipeline v2.
> Nội dung chuyên môn bên dưới dùng bình thường, nhưng **ba loại tham chiếu trong đó đã lỗi** — bỏ qua chúng,
> đừng đi tìm.
>
> **1. Skill không tồn tại trong bộ này.** `project-docs-contract` · `project-docs-workflow` ·
> `project-docs-prd` · `project-docs-overview` · `project-docs-uc` · `project-docs-fr` ·
> `project-docs-wireframes` · `project-docs-flows` · `project-docs-roadmap` · mọi `spec-*` · mọi
> `execution-*` · `ui-redesign` · `quick-*` · `dev-spec-driven` · `ios-debug` · `ios-icon-gen` · `mcp-xcode`.
> Chúng bị loại **có chủ đích** vì thuộc phạm vi sau bàn giao. Danh sách đầy đủ ở `.claude/KIT_MANIFEST.md`.
> Gặp câu *"phải đọc skill X trước"* mà X nằm trong danh sách này thì **bỏ qua câu đó**, không dừng, không đi tìm.
>
> **2. Đường dẫn `.claude/specs/<tên dự án>/...`** — cấu trúc của app-spec, **không có** ở đây.
> Bộ này ghi tài liệu ra `docs/<thư-mục-phase>/<doc_id>_<TÊN>.md`. Danh sách 61 tài liệu ở `docs/_INDEX.md`.
>
> **3. Bảng ánh xạ 1:1 gate→file** kiểu `gate-prd → PRD.md`. Pipeline v2 có 61 tài liệu và 12 cổng G0–G11;
> cổng đọc từ khối `QUALITY-GATE-MANIFEST` ở **cuối template tương ứng**, không từ bảng cứng.
>
> **Đây là skill CHIỀU SÂU.** Nó không sở hữu tài liệu nào, không cấp ID, không gọi cổng. Vai của nó là làm
> skill phụ trách phase hiểu sâu hơn. Mọi thứ ghi ra file vẫn do skill phụ trách phase quyết định.


# SwiftUI MVVM Structure (User-Driven)

## Non-Negotiable Rules (MUST / MUST NOT)

These are enforced by the **Structure Compliance Gate** at the bottom of this skill. Execution
skills run that gate; a violation marks the task `blocked`.

- **MUST** place every new/changed file in the canonical tree: app entry under `App/`, cross-app
  code under `Core/`, feature code under `Features/[Feature]/{Views,ViewModels,Models,Services}/`,
  reusable UI under `.claude/shared/Components/[Type]/`, styles under `shared/Styles/`.
- **MUST** give each feature its own folder with the four subfolders when it has that content.
- **MUST** follow the naming table exactly (`[Feature]View.swift`, `[Feature]ViewModel.swift`,
  `[Entity].swift`, `[Name]Service.swift`, `[Type]+Extensions.swift`).
- **MUST** respect dependency direction `View → ViewModel → Service → Model` (one-way only).
- **MUST NOT** put business logic, networking, or persistence inside a `View`.
- **MUST NOT** scatter feature files outside their feature folder or dump shared UI into a feature.
- **MUST NOT** impose Clean Architecture / heavy patterns unless the user explicitly asks.

## Table of Contents
- [1. Directory Structure](#1-directory-structure) ... L15-L40
- [2. Naming Conventions](#2-naming-conventions) ..... L42-L80
- [3. Organization Rules](#3-organization-rules) ..... L82-L110
- [4. Feature Example](#4-feature-example) ........... L112-L140

---

## 1. Directory Structure

```
ProjectName/
├── App/
│   └── ProjectNameApp.swift
├── Core/
│   ├── Extensions/
│   ├── Utilities/
│   └── Network/
├── Features/
│   └── FeatureName/
│       ├── Views/
│       ├── ViewModels/
│       ├── Models/
│       └── Services/
├── .claude/shared/
│   ├── Components/
│   ├── Styles/
│   └── Modifiers/
├── Resources/
└── Tests/
```

### Folder Purposes

| Folder | Purpose |
|--------|---------|
| `App/` | App entry point, app-level configuration |
| `Core/` | Shared code across app (Extensions, Network, Utilities) |
| `Features/` | Feature modules (Authentication, Home, Profile...) |
| `.claude/shared/` | Reusable UI components (Buttons, Cards, Modifiers) |
| `Resources/` | Assets, Localizable, Info.plist |
| `Tests/` | Unit tests, UI tests |

---

## 2. Naming Conventions

### Folder Naming
- `Features/` - Feature modules by functionality
- `Core/` - App-wide shared code
- `.claude/shared/` - Reusable UI components
- `Services/` - Business logic, API services
- `Resources/` - Assets, Localizable, Info.plist

### File Naming

| Type | Convention | Example |
|------|------------|---------|
| View | `[Feature]View.swift` | `LoginView.swift` |
| ViewModel | `[Feature]ViewModel.swift` | `LoginViewModel.swift` |
| Model | `[EntityName].swift` | `User.swift` |
| Service | `[Name]Service.swift` | `AuthService.swift` |
| Extension | `[Type]+Extensions.swift` | `String+Extensions.swift` |
| Component | `[DescriptiveName].swift` | `PrimaryButton.swift` |
| Protocol | `[Name]Protocol.swift` | `AuthServiceProtocol.swift` |

### Component Naming

| Type | Location | Example |
|------|----------|---------|
| Button | `.claude/shared/Components/Buttons/` | `PrimaryButton.swift` |
| Input | `.claude/shared/Components/Inputs/` | `PrimaryTextField.swift` |
| Card | `.claude/shared/Components/Cards/` | `ItemCard.swift` |
| Modal | `.claude/shared/Components/Modals/` | `ConfirmationModal.swift` |
| Feedback | `.claude/shared/Components/Feedback/` | `LoadingView.swift` |

---

## 3. Organization Rules

### MVVM Responsibilities

| Layer | Responsibility | Contains |
|-------|----------------|----------|
| View | UI only, no logic | SwiftUI views, layout, styling |
| ViewModel | State + business logic | @Published properties, methods |
| Model | Data structure only | Structs, Codable, Identifiable |
| Service | API + data persistence | Network calls, local storage |

### Rules

1. Each feature is a separate folder in `Features/`
2. Each feature has subfolders: `Views/`, `ViewModels/`, `Models/`, `Services/`
3. View contains UI only, no business logic
4. ViewModel contains state and business logic
5. Model is data structure only
6. Service handles API and data persistence
7. Components in `.claude/shared/` are reusable across features

### Dependencies Direction

```
View → ViewModel → Service → Model
  ↓         ↓          ↓
  UI      Logic      Data
```

- View depends on ViewModel
- ViewModel depends on Service
- Service depends on Model
- Model has no dependencies

### Implementation Approach (User-Driven)

**Follow user's explicit intent:**
- If user requests "logic first": start with Models/Services, then ViewModels, then Views
- If user requests "UI first": start with Views/ViewModels wiring, then harden logic
- If user has no preference: follow existing codebase patterns or discuss trade-offs

**Pattern usage is optional, not enforced:**
- Use Singleton only for genuine global state (e.g., SessionManager, AppState)
- Use Delegate for 1-1 callbacks (e.g., form submission, coordinator events)
- Use Observer (@Published/Combine) for reactive state changes
- Use Dependency Injection (protocol + constructor) for testability when needed
- Avoid over-engineering; prefer simplicity that juniors can understand

---

## 4. Feature Example

### Authentication Feature

```
Features/
└── Authentication/
    ├── Views/
    │   ├── LoginView.swift
    │   ├── RegisterView.swift
    │   └── Components/
    │       ├── AuthHeader.swift
    │       └── SocialLoginButtons.swift
    ├── ViewModels/
    │   ├── LoginViewModel.swift
    │   └── RegisterViewModel.swift
    ├── Models/
    │   ├── User.swift
    │   ├── LoginRequest.swift
    │   └── LoginResponse.swift
    └── Services/
        ├── AuthService.swift
        └── AuthServiceProtocol.swift
```

### File Contents Overview

| File | Contains |
|------|----------|
| `LoginView.swift` | UI layout, bindings to ViewModel |
| `LoginViewModel.swift` | @Published state, login(), validate() |
| `User.swift` | User struct with Codable |
| `AuthService.swift` | API calls for login, register |

---

## Checklist

### When creating new feature:
- [ ] Create folder in `Features/[FeatureName]/`
- [ ] Create subfolders: `Views/`, `ViewModels/`, `Models/`, `Services/`
- [ ] Follow naming conventions
- [ ] Keep View logic-free
- [ ] Keep Model data-only

### When creating new screen:
- [ ] Create `[Name]View.swift` in `Views/`
- [ ] Create `[Name]ViewModel.swift` in `ViewModels/`
- [ ] Create models if needed in `Models/`
- [ ] Add Preview for View

### When creating reusable component:
- [ ] Place in `.claude/shared/Components/[Type]/`
- [ ] Make it configurable via parameters
- [ ] Add Preview
- [ ] Document usage

---

## Autopilot Integration Contract

When used with spec agents:
- `design.md` sections define feature modules and file plan based on user intent.
- `tasks.md` Task Registry must reference real paths under this structure.
- Task order follows user's explicit direction (not a hardcoded template):
  - If user wants logic-first: Models/Services → ViewModels → Views → Integration
  - If user wants UI-first: Views → ViewModels → Logic hardening → Integration
  - If user has preference: follow their stated order

Required alignment:
- Every task file path must map to `Features/[FeatureName]/...` or shared folders.
- Respect existing codebase patterns when present.
- Do not impose Clean Architecture or complex patterns unless user explicitly requests.

---

## Structure Compliance Gate (Required)

Execution skills (`execution-implement`, `execution-quick`, `execution-quality-gates`) run this gate
whenever a task **creates or moves a file**. This gate is the single source of truth for file/folder
placement — the executor must not re-derive its own conventions.

**Checklist (every item must pass):**
- [ ] Each created/changed path maps to a canonical location:
      `App/`, `Core/{Extensions,Utilities,Network}/`, `Features/[Feature]/{Views,ViewModels,Models,Services}/`,
      `.claude/shared/Components/[Type]/`, `shared/Styles/`, `shared/Modifiers/`, `Resources/`, `Tests/`.
- [ ] File name matches the Naming Conventions table for its type.
- [ ] Feature code lives under its own `Features/[Feature]/` folder (not scattered, not in another feature).
- [ ] Reusable UI is under `shared/Components/[Type]/`, not embedded in a single feature, and vice-versa.
- [ ] `View` files contain UI only — no networking, persistence, or business logic (that belongs in ViewModel/Service).
- [ ] Dependency direction stays `View → ViewModel → Service → Model` (no back-edges).

**BLOCK conditions** → mark task `blocked`, do not set `done`:
- A file is placed off the canonical tree, misnamed, or in the wrong layer.
- Business logic / IO leaked into a `View`.
- A reusable component was created inside a feature folder (or a feature file dumped into `shared/`).

**Evidence line** (required in task notes for any file-creating task):
```
Structure: <path> → <layer> OK | violations: none
```
If violations exist, list them instead of `none` and block.
