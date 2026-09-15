---
doc_id: _DOCUMENTATION_STANDARD
title: Chuẩn quản lý tài liệu — bản trong dự án
owner: PO
version: 2.0.0
status: approved
---

# Chuẩn quản lý tài liệu

Bản rút gọn đặt trong dự án để tài liệu **tự giải thích được** mà không cần người viết ngồi cạnh.
Nguồn: Pipeline v2 và Chuẩn quản lý tài liệu của tổ chức.

## Ba nguyên tắc không được vi phạm

**Checkpoint.** Mỗi tài liệu là một điểm dừng. Không tạo nhiều tài liệu trong một lượt.
Chỉ file `status: approved` được dùng làm đầu vào cho tài liệu khác.

**Truy nguyên.** Mọi hạng mục truy được về một vấn đề người dùng có bằng chứng, và truy tiếp xuống tới ca
nghiệm thu. Không có hạng mục mồ côi ở bất kỳ đầu nào của chuỗi.

**Một nguồn sự thật.** Mỗi thông tin do đúng một tài liệu sở hữu. Tài liệu khác trích ID, không sao chép nội dung.

## Quy ước đặt tên

`PP-NN_TÊN_VIẾT_HOA.md` — `PP` số phase, `NN` số thứ tự trong phase.

Thêm file mới thì cấp số **tiếp theo còn trống**, không chèn giữa, không đánh số lại.
File bị bỏ thì giữ số ở trạng thái `archived`, không tái sử dụng.
File điều phối bắt đầu bằng `_` để luôn nằm trên cùng khi sắp xếp.

## Front-matter bắt buộc

```yaml
---
doc_id: 06-02
title: Functional Requirements
phase: 06-breakdown
skill: product-breakdown
profile: Bắt buộc
owner: PO
version: 0.1.0
status: draft
depends_on: [06-01]
feeds: [07-05, 08-01, 13-04]
id_prefix: [FR]
gate: G5
in_handover: true
confidence: low
---
```

Vòng đời `status`: `draft` → `in-review` → `approved` → `superseded` / `archived`.

`version`: tăng số cuối khi sửa nhỏ · số giữa khi nội dung ảnh hưởng tài liệu khác · số đầu khi cấu trúc đổi.

`confidence` nói về độ tin cậy **nội dung**, không phải mức hoàn thiện văn bản. `approved` mà `confidence: low`
là hợp lệ — nghĩa là đã đồng ý đi tiếp trên cơ sở giả định, và giả định đó phải có ở `_ASSUMPTION_REGISTER.md`.

## Ai sở hữu thông tin gì

Bảng này giải quyết tranh chấp khi hai tài liệu nói khác nhau. Chỉ tài liệu sở hữu được định nghĩa.

| Thông tin | File sở hữu |
| --- | --- |
| Phạm vi và danh sách bị cấm | `00-02_SCOPE_LOCK.md` |
| Đối thủ | `02-01_COMPETITOR_LANDSCAPE.md` |
| Insight | `04-03_USER_INSIGHTS.md` |
| Persona | `04-05_PERSONA.md` |
| Aha moment | `04-06_CUSTOMER_JOURNEY.md` |
| Danh sách tính năng, phạm vi MVP | `05-01_PRD.md` |
| Công thức và quy tắc nghiệp vụ | `06-04_BUSINESS_RULES.md` |
| Ngưỡng chất lượng | `06-03_NON_FUNCTIONAL_REQUIREMENTS.md` |
| Hành vi từng trạng thái quyền | `06-05_PERMISSION_AND_DATA_NEEDS.md` |
| Mã màn hình | `08-01_SCREEN_INVENTORY.md` |
| Trạng thái màn hình | `08-02_STATE_MATRIX.md` |
| Giá và gói subscription | `09-02_MONETIZATION_PAYWALL_SPEC.md` |
| Mọi chuỗi văn bản | `09-06_COPY_DECK.md` |
| Tên và thuộc tính event | `10-02_EVENT_TAXONOMY.md` |
| Định nghĩa activation / retention | `10-03_FUNNEL_DEFINITION.md` |
| Luồng, mũi tên, điều kiện rẽ nhánh | `wireframes/flow-FLOW-xxx.html` — **không** mô tả lại bằng lời ở `08-03` |
| Nội dung và thứ tự nội dung từng màn | `wireframes/<SCR>_<ST>_*.html` |
| Chức năng, vào từ đâu, bấm gì ra đâu, đường thoát | khối `.w-notes` trong chính file màn |
| Hướng thị giác, hệ màu, hệ chữ | `12-00_UI_RESEARCH.md` |
| Token và component | `12-02_DESIGN_SYSTEM_AND_A11Y.md` |
| Từ vựng và cách gọi | `_GLOSSARY.md` |
| Kiến trúc, API, schema | `tech-input/` — **Dev sở hữu** |

Hệ quả thực tế: **giá subscription chỉ được viết bằng số ở đúng một chỗ.** PRD nói "theo `PLN-001`".
Copy deck nói "theo `PLN-001`". Khi giá đổi, sửa một chỗ.

## Ba quy tắc thứ tự

1. **Screen inventory trước wireframe.**
2. **UX flow không được sinh màn hình mới** — thiếu màn thì qua `08-04_MISSING_SCREEN_REPORT.md`.
3. **KPI trước event.**

## Hai mục bắt buộc ở mọi tài liệu — để người vai trò khác đọc được

| Mục | Vị trí | Nội dung |
| --- | --- | --- |
| `0. Đọc nhanh` | đầu tài liệu | bốn dòng viết **không thuật ngữ**: tài liệu này là gì · ai cần đọc · đọc xong phải biết gì · quyết định nào chốt ở đây |
| `Thuật ngữ dùng trong tài liệu này` | cuối tài liệu | mọi thuật ngữ và tiền tố mã có dùng, kèm nghĩa một câu |

Bộ tài liệu này có **ba nghề cùng đọc**: Product Owner, Designer, Dev. Ai cũng viết bằng tiếng nghề mình và
mặc định người khác hiểu. Thực tế là người ở nghề khác lướt qua chỗ lạ, tưởng mình hiểu, rồi vẫn duyệt —
và sáu tuần sau mới lộ ra hai bên hiểu hai kiểu.

**Thuật ngữ giữ nguyên.** Diễn giải là **thêm vào**, không phải thay thế: người trong nghề vẫn cần đúng từ
đó để tra cứu và để nói chuyện với bên ngoài. Nguồn nghĩa: `_GLOSSARY.md` mục *Thuật ngữ chuyên môn* và
`_ID_REGISTRY.md` mục *Bảng prefix*. Thiếu từ thì thêm vào từ điển, đừng bỏ qua.

`validate_docs.py` kiểm hai chiều: dùng mà không liệt kê là **LỖI**; liệt kê mà không dùng là cảnh báo.

## Khi nào chuẩn này là quá nhiều

Chạy đủ 61 tài liệu cho một MVP là quá nhiều và sẽ tạo ra tài liệu không ai đọc.

Đang kiểm chứng nhu cầu, chưa quyết làm hay không → **profile Lean**, khoảng 12 file.
Sản phẩm rất nhỏ, một tính năng, công cụ nội bộ → chỉ cần `06-02` FR, `08-01` screen inventory,
`08-02` state matrix, `13-04` acceptance criteria.

Nguyên tắc phân xử: **một tài liệu chỉ đáng tồn tại nếu thiếu nó thì có người phải hỏi lại, hoặc có người sẽ
làm sai.** Không thoả một trong hai thì nó là chi phí thuần.

Dấu hiệu tài liệu thừa: có file `approved` mà không ai trích dẫn trong ba tuần. Ghi nhận lại và loại nó khỏi
profile ở dự án sau.
