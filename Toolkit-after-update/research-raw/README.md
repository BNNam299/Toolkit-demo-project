# research-raw — nguyên liệu thô của bạn

Thư mục này là **tài sản của bạn**, giống `tech-input/` là tài sản của Dev.

AI **đọc** thư mục này nhưng **không sửa** nội dung trong đây. Lý do: đây là bằng chứng. Bằng chứng bị AI
viết lại thì không còn là bằng chứng.

## Dùng vào hai việc

**1. Nạp nghiên cứu đã có sẵn từ trước.** Dự án đã nghiên cứu rồi, giờ chỉ cần chạy bộ để ra bản hoàn
thiện: bỏ hết file cũ vào đây — Word, Excel, PDF, ảnh, export từ Notion, gì cũng được.

Rồi gõ cho Claude:

```
Đừng viết tài liệu nào cả.
Đọc hết research-raw/, rồi lập bảng đối chiếu với docs/_INDEX.md:
- mỗi tài liệu trong _INDEX: nội dung đã có ở file nào, mục nào
- mức độ phủ: đủ / một phần / không có
- chỗ nào là dữ liệu thật có dẫn nguồn, chỗ nào là kết luận không có nguồn
Báo cáo dạng bảng, sắp theo phase. Chưa ghi gì vào docs/.
```

Có bản đồ rồi mới lấp từng tài liệu, **theo thứ tự phase**, mỗi lượt một tài liệu. Khi lấp phải nói rõ:
*"chỉ dùng nội dung có trong research-raw, không bổ sung kiến thức chung"* — nếu không, Claude sẽ điền chỗ
trống bằng những thứ nghe hợp lý mà không phải nghiên cứu của bạn, và bạn sẽ không phân biệt được.

Hai thứ gần như chắc chắn **không lấp được** từ nghiên cứu cũ: tầng bằng chứng dưới persona (nếu không còn
bản ghi phỏng vấn thì đó là **proto-persona**, phải ghi rõ), và `03-05` khả thi công nghệ (phải làm mới,
cần Dev trả lời qua `tech-input/TECH-00`).

**Có cả một bộ tài liệu hoàn chỉnh từ bộ khác** — PRD, use case, FR, wireframe, roadmap — thì đó là việc
khác và nặng hơn: bộ cũ có **hệ mã ID riêng**, và chính hệ mã đó là chỗ dễ phá truy nguyên nhất. Đặt file vào
`ho-so-cu/` rồi gõ `/import-legacy bản đồ`. Quy trình tám bước ở `.claude/commands/import-legacy.md`, phiếu
công tác ở `ho-so-cu/_MAP.md`.

**2. Chứa dữ liệu bạn phải tra tay ở công cụ AI không vào được.** Xem hai file `SENSOR_TOWER_*` bên cạnh.

## Quy ước đặt tên

Đặt tên có ngày để biết cái nào mới: `2026-08-12_sensor-tower_calorie-apps.xlsx`.

Gợi ý chia thư mục con khi nhiều file:

```
research-raw/
├── SENSOR_TOWER_REQUEST.md    ← Claude điền: cần số gì
├── SENSOR_TOWER_DATA.md       ← bạn gõ tay, chỉ khi ít số
├── sensor-tower/              ← NHIỀU DATA thì bỏ hết vào đây
│   ├── _MANIFEST.md           mục lục file — Claude đề xuất, bạn sửa
│   ├── _EXTRACTED.md          số Claude đọc được, bạn xác nhận
│   ├── 2026-08-12_myfitnesspal_downloads_VN.csv
│   ├── 2026-08-12_myfitnesspal_retention_VN.png
│   └── ...
├── ho-so-cu/                  ← BỘ TÀI LIỆU hoàn chỉnh từ bộ khác  → /import-legacy
├── nghien-cuu-cu/             ← tài liệu rời đã có từ trước
├── review-thu-thap/           ← review copy về, kèm URL
├── thu-hoach/                 ← Codex/OpenCode đào về, xem README trong đó
├── man-hinh-doi-thu/          ← ảnh màn hình đối thủ, mỗi app một thư mục  → 07-00
└── moodboard/                 ← ảnh tham chiếu UI, màu, chữ, thành phần    → 12-00
```

### Ba thư mục ảnh, ba mục đích khác nhau

| Thư mục | Chụp/lấy cái gì | Phục vụ tài liệu | Đọc trước |
| --- | --- | --- | --- |
| `man-hinh-doi-thu/` | **luồng** của app đối thủ, theo đúng thứ tự bấm | `07-00` UX Research | `_MANIFEST.md` |
| `moodboard/` | **thị giác**: màu, chữ, thành phần, màn đẹp, và cả màn không thích | `12-00` UI Research | `_MANIFEST.md` |
| `sensor-tower/` | số liệu tra tay | `01-01` `02-01` | `_MANIFEST.md` |

Hai thư mục ảnh đầu **quét hai lần vào hai lúc khác nhau**: `07-00` đọc `man-hinh-doi-thu/` để hiểu luồng
và kiến trúc thông tin; `12-00` đọc lại đúng những ảnh đó để xem *từng chức năng họ vẽ ra sao*. Đừng gộp
hai lần quét — đọc thị giác quá sớm là cách chắc nhất để sao chép giao diện trước khi hiểu vì sao nó có.

### Ba lớp, và ai được sửa lớp nào

Khi dữ liệu nhiều — ảnh chụp dashboard, file xuất, PDF báo cáo — đừng gõ tay vào `SENSOR_TOWER_DATA.md`.
Bỏ hết vào `sensor-tower/` rồi để Claude đọc. Luồng gồm ba lớp:

| Lớp | File | Ai viết | Ai sửa được |
| --- | --- | --- | --- |
| Thô | file bạn nộp trong `sensor-tower/` | bạn | chỉ bạn — AI **không sửa** |
| Bản đọc | `sensor-tower/_EXTRACTED.md` | **AI** | AI viết, bạn xác nhận từng dòng |
| Tài liệu | `docs/…` | AI | chỉ số **đã xác nhận** mới được vào |

Lý do có lớp giữa: ai đó phải chuyển số từ ảnh sang dạng có cấu trúc. Nếu AI ghi thẳng vào `docs/` thì bạn
mất cơ hội bắt chỗ nó đọc lệch — mà đọc lệch số từ biểu đồ không có nhãn là chuyện xảy ra thật.

Câu để khởi động:

```
Đọc research-raw/sensor-tower/. Liệt kê file, mở từng file,
đề xuất điền _MANIFEST.md rồi ghi số đọc được vào _EXTRACTED.md.
Mỗi dòng ghi rõ file nguồn, cách đọc, và độ tin.
Đọc lại cho tôi những dòng độ tin thấp trước khi dùng vào tài liệu nào.
```

**Xuất được CSV hay XLSX thì đừng chụp ảnh.** Claude đọc biểu đồ trong ảnh bằng cách suy theo chiều cao cột
so với trục — sai số thật khi biểu đồ không in số trên từng điểm.

## Ba quy tắc

**Luôn kèm nguồn.** Mỗi file hoặc mỗi khối dữ liệu ghi lấy từ đâu và ngày nào. Không có nguồn thì AI không
được dán nhãn `[FACT]` cho nội dung đó.

**Trích nguyên văn, đừng tóm tắt trước.** Bản tóm tắt của bạn cũng là một tầng suy luận. Cứ dán nguyên câu
người dùng viết, để AI đối chiếu.

**Số của công cụ bên thứ ba là ước lượng.** AppStoreSpy, Sensor Tower, Data.ai — ghi nguồn dạng
*"ước lượng theo Sensor Tower, ngày 12/08/2026"*, không ghi như số liệu nội bộ của đối thủ.
