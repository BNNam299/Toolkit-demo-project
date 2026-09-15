---
description: Nạp bộ tài liệu cũ của một dự án đã chạy vào bộ này, không phá truy nguyên
argument-hint: "[bản đồ | lấp <doc_id> | trạng thái]"
---

# /import-legacy — nạp hồ sơ cũ vào Pipeline v2

> **File này là markdown thuần.** Claude Code gọi bằng `/import-legacy`. Codex, OpenCode và mọi agent khác
> dùng được y hệt: *"làm theo `.claude/commands/import-legacy.md`"*.

Dùng khi dự án **đã có bộ tài liệu hoàn chỉnh** viết bằng bộ khác — PRD, use case, FR, wireframe, roadmap —
và giờ muốn chạy tiếp bằng bộ này.

Khác với `research-raw/README.md` mục 1: ở đó là **nghiên cứu rời** (review, ảnh, export). Ở đây là **một bộ
tài liệu có cấu trúc riêng, có hệ mã ID riêng**. Chính hệ mã đó là chỗ dễ phá truy nguyên nhất.

## Quy tắc bất di bất dịch

**1. Không bao giờ dán file cũ vào `docs/`.** `docs/` chỉ chứa tài liệu sinh theo template của bộ này, có
front-matter 13 trường và khối mục theo manifest. Dán file cũ vào đó thì `validate_docs.py` sập, `_INDEX`
lệch, và không ai biết đâu là bản đã qua cổng.

File cũ nằm ở **`research-raw/ho-so-cu/`** — nguyên vẹn, không sửa. Nó là **bằng chứng**, cùng hạng với
review đã đào và ảnh chụp.

**2. Không đánh số lại ID cũ.** Đây là quy tắc số một của bộ (`_ID_REGISTRY`), và nó áp cả cho ID nhập từ
ngoài. Có `FR-001`…`FR-066` cũ thì **nhận nguyên**, rồi đặt *Số cuối đã cấp* của prefix `FR` thành `066`.
ID mới bắt đầu từ `067`. Đánh số lại là làm chết mọi tham chiếu trong lịch sử chat, ticket, commit của dự án.

**3. Prefix không có trong `_ID_REGISTRY` thì phải xử, không được để lọt.** Bộ cũ có thể dùng `WF`, `TF`,
`SF`, `AF`, `ERR`, `VR`, `R`… Bộ này không có. Hai lựa chọn cho mỗi prefix, ghi ở mục 3 của `_MAP.md`:
**đổi sang prefix tương đương** (kèm bảng ánh xạ từng mã), hoặc **thêm prefix mới vào `_ID_REGISTRY`** nếu nó
mang một loại thông tin bộ này chưa có.

`validate_docs.py` là lưới an toàn ở đây: prefix lạ trong `docs/` sẽ ra **CẢNH BÁO "chưa kiểm được"**. Thấy
cảnh báo đó nghĩa là còn mã cũ lọt vào — chưa xử xong.

**4. Không kế thừa trạng thái `approved`.** Tài liệu cũ chưa từng đi qua 12 cổng của bộ này. Bản lấp đầu tiên
luôn là `draft`. Muốn `approved` thì phải chạy cổng thật, hoặc **bỏ cổng có ý thức** và ghi vào `_INDEX` mục 6.

## Bước 1 — Đặt file và kiểm kê

```
research-raw/ho-so-cu/
├── _MAP.md                    ← phiếu công tác, bạn và tôi cùng điền
├── PRD.md                     nguyên bản, không sửa
├── Use_Cases.md
├── Wireframes.md
└── … mọi file khác
```

Điền mục 1 của `_MAP.md`: mỗi file cũ một dòng — tên, số dòng, ngày cập nhật cuối, và **phiên bản** nếu bộ cũ
có ghi. Cột *ngày* là cột sẽ dùng ở bước 3.

## Bước 2 — Lập bản đồ phủ, **chưa ghi gì vào `docs/`**

`/import-legacy bản đồ`

Đọc hết `research-raw/ho-so-cu/`, rồi điền mục 2 của `_MAP.md`: với **từng** tài liệu trong `docs/_INDEX.md`,
nội dung đã có ở file nào, mục nào, và mức phủ **Đủ / Một phần / Không có**.

Ba cột phải điền thật, không được đoán:

| Cột | Vì sao |
| --- | --- |
| **Nguồn** | file + số mục. Không ghi được nguồn cụ thể nghĩa là chưa đọc, chỉ đang suy |
| **Mức phủ** | Đủ / Một phần / Không có |
| **Có nguồn hay không** | nội dung cũ đó **có dẫn nguồn** hay là kết luận trơn |

Cột thứ ba là cột quan trọng nhất. Bộ cũ có thể rất đầy ở chỗ có nguồn và **bịa hoàn toàn** ở chỗ không có
nguồn, mà nhìn bề ngoài hai chỗ giống nhau. Chỗ không có nguồn khi lấp sang phải gắn `[ASM]`, không được để
thành `[FACT]`.

**Dừng ở đây, báo cáo bảng, chờ người dùng đọc.** Không lấp gì.

## Bước 3 — Tìm mâu thuẫn trong hồ sơ cũ, trước khi lấp

Đây là bước **không được bỏ**, và là bước sinh ra cả lệnh này.

Một bộ tài liệu đã qua nhiều bản thường có phần được viết lại và phần **không ai cập nhật theo**. Lấp sang bộ
mới mà không phát hiện thì mâu thuẫn được sao chép nguyên vẹn, và từ đó nó có vẻ chính danh vì đã qua cổng.

Điền mục 4 của `_MAP.md`. Bốn phép soi, làm theo đúng thứ tự này:

1. **So bản mới nhất với bản cũ.** Bộ cũ có ghi *"section này viết lại ở vX"* ở đâu không? Nếu có, mọi section
   **không** được viết lại đều là nghi phạm.
2. **So định vị sản phẩm với persona và nhu cầu người dùng.** Persona có đang mô tả đúng sản phẩm hiện tại,
   hay mô tả một sản phẩm đã bị bỏ?
3. **So bảng bằng chứng với các kết luận.** Có số nào bị đánh dấu sai/nghi vấn trong bảng bằng chứng mà vẫn
   được dùng như số thật ở chỗ khác?
4. **So các con số tổng.** Số rủi ro, số màn, số yêu cầu ghi ở phần tóm tắt có khớp phần chi tiết không?

Mỗi mâu thuẫn tìm được: một dòng, kèm **hai vị trí** và **phán quyết bên nào đúng**. Chưa biết bên nào đúng
thì ghi `OQ` vào `docs/_OPEN_QUESTIONS.md` và **không lấp phần đó** cho tới khi người dùng chốt.

Không tìm thấy mâu thuẫn nào thì ghi thẳng *"đã soi bốn phép, không thấy"* — đừng để trống, vì để trống trông
giống hệt chưa làm.

## Bước 4 — Chốt hệ mã

Điền mục 3 của `_MAP.md`, rồi **cập nhật `docs/_ID_REGISTRY.md`**:

- Prefix trùng tên và trùng nghĩa (`UC`, `FR`, `NFR`, `BR`): nhận nguyên số cũ, đặt *Số cuối đã cấp*.
- Prefix cũ không có trong bộ này: chọn **đổi** hay **thêm**, ghi lý do một dòng.
- Đổi thì phải có **bảng ánh xạ từng mã**, không chỉ ánh xạ prefix — `WF-017 → SCR-017` phải liệt kê ra, vì
  người ta sẽ tra ngược.

Ghi một `DEC` vào `docs/_DECISION_LOG.md`: đã nhận hệ mã cũ, prefix nào đổi thành gì, số bắt đầu cấp mới.

## Bước 5 — Lấp từng tài liệu, **theo thứ tự phase**

`/import-legacy lấp 05-01`

Mỗi lượt **một tài liệu**, đúng luật của bộ. Khác biệt duy nhất so với viết mới:

**Chỉ dùng nội dung có trong `research-raw/ho-so-cu/`.** Không bổ sung kiến thức chung. Chỗ hồ sơ cũ không có
thì để trống và ghi *"hồ sơ cũ không có"* — **không** điền bằng thứ nghe hợp lý. Đây là chỗ trượt nguy hiểm
nhất của cả quy trình nạp: bản lấp trông đầy đủ nhưng một nửa là AI tự viết, và sáu tuần sau không ai phân
biệt được nữa.

Khối báo cáo Lớp 2 thêm một dòng:

```
Lấp từ hồ sơ cũ: <file + mục>
Phần tôi để trống vì hồ sơ cũ không có: <liệt kê, hoặc "không có">
Phần tôi gắn [ASM] vì hồ sơ cũ không dẫn nguồn: <liệt kê>
```

`last_updated` ghi **ngày lấp**, không phải ngày của file cũ — để `check_stale_inputs` hoạt động đúng từ đây.

## Bước 6 — Ba thứ gần như chắc chắn phải làm lại, không lấp được

| Không lấp được | Vì sao | Phải làm gì |
| --- | --- | --- |
| Tầng bằng chứng dưới persona | không còn bản ghi phỏng vấn thì persona cũ là suy đoán | ghi rõ **proto-persona**, hoặc chạy lại phase 04 |
| `03-05` khả thi công nghệ | Dev chưa từng phán quyết theo khuôn này | làm mới, Dev trả lời qua `tech-input/TECH-00` |
| `12-00` nghiên cứu UI | bộ cũ thường chọn phong cách không có tài liệu lý do | làm mới, cần `research-raw/moodboard/` |

Thêm hai thứ hay thiếu: **`08-02` mục 1b** (trạng thái theo ngữ cảnh người dùng) và **`05-01` danh sách không
được cắt** — bộ cũ gần như không bao giờ có hai thứ này.

## Bước 7 — Quyết định về cổng

Hồ sơ cũ **không** kế thừa được cổng. Với mỗi cổng đã đi qua trong đời sản phẩm, chọn một và ghi vào
`docs/_INDEX.md` mục 6:

| Lựa chọn | Khi nào chọn | Ghi gì |
| --- | --- | --- |
| **Chạy cổng thật** | có đủ bằng chứng trong hồ sơ cũ để tick checklist | không cần ghi gì thêm |
| **Bỏ cổng có ý thức** | sản phẩm đã chạy, chạy lại cổng không đổi được gì | cổng nào, vì sao, **rủi ro kèm theo** |
| **Chạy lại từ phase đó** | phát hiện mâu thuẫn ở bước 3 làm sập kết luận | ghi `CHG` và `DEC` |

Cột *rủi ro kèm theo* là cột đừng bỏ trống. Bỏ `G3` nghĩa là tầng người dùng của dự án này không có bằng
chứng — đó là một rủi ro thật, không phải một thủ tục.

## Bước 8 — Kiểm

```
python .claude/scripts/validate_docs.py
```

Ba cảnh báo đặc trưng của việc nạp hồ sơ cũ, và ý nghĩa:

| Báo | Nghĩa |
| --- | --- |
| **prefix chưa kiểm được** (`WF`, `TF`, `ERR`…) | còn mã cũ lọt vào `docs/` — quay lại bước 4 |
| **ID trích mà chưa cấp** | đã nhận số cũ nhưng chưa cập nhật `_ID_REGISTRY` |
| **ĐẦU VÀO MỚI HƠN** | lấp `06-02` trước rồi mới lấp `05-01` — đọc lại `06-02` |

Cảnh báo thứ ba là lý do bước 5 nói **theo thứ tự phase**. Lấp ngược thì tài liệu dưới đứng trên một đầu vào
sẽ đổi sau đó.

`/import-legacy trạng thái` — in bảng mục 2 của `_MAP.md` kèm tài liệu nào đã lấp, còn bao nhiêu, không lấp gì.
