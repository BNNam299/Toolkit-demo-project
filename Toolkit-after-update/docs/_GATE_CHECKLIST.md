---
doc_id: _GATE_CHECKLIST
title: 12 cổng
owner: PO
version: 0.1.0
status: draft
---

# _GATE_CHECKLIST — 12 cổng

Mỗi cổng là một điểm dừng bắt buộc. Fail thì sửa, không đi tiếp.
Bỏ qua được, nhưng phải ghi vào `_INDEX.md` mục 6: cổng nào, vì sao, rủi ro kèm theo.

---

## G0 — Brief đã khoá · sau phase 00

- [ ] `00-01_PROJECT_BRIEF.md` có `status: approved`
- [ ] `00-02_SCOPE_LOCK.md` có `status: approved`
- [ ] **Danh sách bị cấm không rỗng**
- [ ] Mục "ngoài phạm vi, đã cân nhắc" có ít nhất một mục kèm lý do
- [ ] Đã chọn profile và ghi vào `_INDEX.md` mục 1
- [ ] Mọi câu chưa trả lời được đã gắn `[ASM]` và có dòng ở `_ASSUMPTION_REGISTER.md`

## G1 — Cơ hội có bằng chứng · sau phase 01–02

- [ ] Mỗi need cluster có **≥3 bản ghi** từ **≥2 nguồn khác nhau**
- [ ] Mỗi pain point trong `01-02` có link hoặc trích dẫn nguồn kiểm chứng được
- [ ] Competitor teardown dựa trên **dùng thật**, không chỉ đọc trang store
- [ ] Số liệu nội bộ đối thủ không có nguồn công khai đã ghi **Không công bố**, không ước đoán
- [ ] Mỗi `GAP` có bằng chứng, không phải suy diễn
- [ ] Số từ công cụ bên thứ ba ghi rõ **ước lượng theo <công cụ>, ngày <ngày>** — không ghi như số nội bộ đối thủ
- [ ] Chỉ số cần tra tay đã gộp vào **một phiếu** `research-raw/SENSOR_TOWER_REQUEST.md`, không hỏi lẻ nhiều lượt
- [ ] Chỉ số người dùng không tra được đã có `[ASM]` hoặc ghi **Không công bố** — AI không tự điền số thay

## G2 — Cơ hội đã kiểm chứng và công nghệ khả thi · sau phase 03

- [ ] **Need Score ≥ 25/35**
- [ ] Concept viết đúng khuôn: *For [ai] who [vấn đề], sản phẩm cung cấp [giải pháp], khác với [thay thế hiện tại], vì [lợi thế]*
- [ ] **Ngưỡng PASS/KILL đặt TRƯỚC khi chạy kiểm chứng**, không đặt sau khi thấy kết quả
- [ ] `13-02_DEV_QUESTION_LOG.md` đã được mở
- [ ] Nếu Need Score không đạt: đã ghi quyết định dừng hoặc xoay hướng vào `_DECISION_LOG.md`

**Khả thi công nghệ — điều kiện thứ hai của cổng này, ngang hàng với Need Score**

- [ ] `03-05_TECH_FEASIBILITY_BRIEF.md` đã liệt kê mọi `CAP` và gắn nhãn **Cốt lõi / Phụ**
- [ ] Mỗi `CAP` mô tả bằng ngôn ngữ **năng lực**, không nêu tên công nghệ — chọn công nghệ là việc của Dev
- [ ] Dev đã nộp `tech-input/TECH-00_FEASIBILITY_SCREEN.md`
- [ ] **Không còn `CAP` nào ở trạng thái `CHƯA TRẢ LỜI`**
- [ ] Phán quyết ở `03-05` mục 5 điền từ `TECH-00`, ghi rõ ngày nhận — không do PO hoặc AI tự phán quyết
- [ ] Nếu có `CAP` **cốt lõi** nhận **KHÔNG KHẢ THI**: kết luận ở mục 6 là **XOAY CONCEPT** hoặc **DỪNG DỰ ÁN**, kèm `DEC`
- [ ] Nếu có `CAP` **KHẢ THI CÓ ĐIỀU KIỆN**: điều kiện đã thành `[DEC]`, và `00-02_SCOPE_LOCK.md` đã cập nhật nếu phạm vi đổi

## G3 — Nghiên cứu đã audit · sau phase 04

- [ ] `04-07_RESEARCH_AUDIT.md` kết luận **đủ điều kiện đi tiếp**
- [ ] Mỗi `INS` rút ra từ **≥2 nguồn** hoặc **≥3 quan sát độc lập**
- [ ] Persona dựa trên **hành vi**, không chỉ nhân khẩu học
- [ ] Đã xác định **aha moment** trong `04-06_CUSTOMER_JOURNEY.md`
- [ ] Persona suy đoán đã ghi rõ là **proto-persona**, không trình bày như có dữ liệu
- [ ] **Mọi `INS`, `JTBD`, `PER`, `JRN` dẫn được về một bản ghi cụ thể** ở `04-02`, hoặc `PN`/`NC` ở phase 01–02,
      hoặc `research-raw/` — **không hạng mục nào dựa trên kiến thức chung về người dùng**
- [ ] Không có chi tiết nào trong persona được thêm cho sinh động mà không có nguồn
- [ ] `04-08` mục 4 *Mâu thuẫn giữa nói và làm* có nội dung, hoặc ghi rõ **chưa quan sát được** kèm lý do
- [ ] Mỗi `EMP` có nguồn cụ thể; ô *Nói gì* là trích nguyên văn, không phải diễn giải

## G4 — PRD đã duyệt · sau phase 05

- [ ] `05-02_PRD_AUDIT.md` **PASS đủ 5 cổng chất lượng**
- [ ] Mọi `FEAT` truy được về `INS` hoặc `JTBD`
- [ ] **PRD không tự khai báo công nghệ** — kiến trúc thuộc Dev
- [ ] Giá cụ thể **không** viết bằng số trong PRD, chỉ trích `PLN-xxx`
- [ ] Phạm vi MVP khớp `00-02_SCOPE_LOCK.md`, không phình
- [ ] Mức ưu tiên dùng đúng **bảng quy đổi** ở `docs/_GLOSSARY.md` — Tier 1 / Must / Cao / P0 là cùng một thứ
- [ ] Mọi trường hợp lệch mức ưu tiên gốc đã ghi vào bảng **Nâng hạ phạm vi** ở `05-01` mục 11, kèm `DEC`
- [ ] `05-01` mục 11 có bảng **Không được cắt trong mọi trường hợp**, ≥1 hạng mục, mỗi hạng mục ghi rõ cắt thì hỏng thế nào

## G5 — Yêu cầu đã phân rã · sau phase 06

- [ ] Mọi `FEAT` có **≥1 `UC`**
- [ ] Mọi `UC` có **≥1 `FR`**
- [ ] Mọi `FR` có **acceptance criteria đo được**
- [ ] AC **không chứa** các từ: nhanh, mượt, dễ dùng, trực quan, đẹp, hợp lý, đầy đủ, tối ưu
- [ ] Mọi `BR` có **công thức kèm ít nhất một ví dụ tính tay**
- [ ] Mọi `UC` có luồng thay thế và luồng ngoại lệ, không chỉ luồng chính
- [ ] Mọi quyền có nhánh **từ chối vĩnh viễn**
- [ ] Mọi `NFR` có **số và điều kiện đo** (thiết bị nào, mạng nào)
- [ ] **Định mức chiều sâu:** mỗi `UC` có ≥1 luồng thay thế và ≥1 luồng ngoại lệ · mỗi `FR` mức **Must** có
      **≥3 acceptance criteria** · mỗi `BR` có ví dụ tính tay và ≥5 trường hợp biên
- [ ] Bảng tổng hợp `06-01` mục 3, `06-02` mục 3, `06-04` mục 2 đã điền đủ — script đếm từ đây

- [ ] `06-00_FEATURE_BRIEF_FOR_DEV.md` đã gửi Dev **trước khi** viết `06-01`, không phải sau
- [ ] Mọi `FEAT` mức **Must** có một khối brief ở `06-00` mục 2
- [ ] Cột *Khả thi* ở `06-00` mục 3 không còn `CHƯA TRẢ LỜI` cho `FEAT` mức Must
- [ ] `FEAT` bị cắt vì không khả thi đã có `CHG` và đã cập nhật `05-01` mục 10 và mục 11

## G6 — Cấu trúc đã duyệt · sau phase 07

- [ ] Đủ các flow bắt buộc: happy path, nhánh thay thế, lỗi, huỷ, từ chối quyền, không dữ liệu, đang tải, rỗng, gián đoạn, người dùng quay lại
- [ ] **Mọi nhánh có kết cục** — không nhánh nào cụt
- [ ] **Không `SCR` ID lạ** — flow không tham chiếu màn hình chưa được cấp mã
- [ ] Mọi node trong IA xuất hiện trong ít nhất một flow
- [ ] Số bước tới giá trị cốt lõi đã đếm và ghi lại
- [ ] `07-00` viết **trước** `07-01`, và mục 0 điền trước khi mô tả app nào
- [ ] Mọi `PAT` có quyết định **Áp dụng / Điều chỉnh / Không dùng**, không để trống
- [ ] **Không `PAT` nào lấy lý do là "vì đối thủ làm vậy"** — phải neo vào `INS` hoặc `JTBD` cụ thể
- [ ] Mọi ảnh dùng làm bằng chứng có ngày chụp; kết luận cần dùng thật mới chắc đã gắn `[ASM]`
- [ ] **Bảng kiểm phụ thuộc phạm vi ở `07-05` mục 4 không còn ô ❌** — mọi `UC` đường phục hồi hoặc
      đường tới hạn của một luồng Tier 1 cũng phải là Tier 1
- [ ] Mỗi lần nâng hoặc hạ tier để xử lý ô ❌ đã có `DEC` và đã cập nhật `05-01` mục 11

## G7 — Kiểm kê màn hình xong · sau phase 08

- [ ] Screen inventory làm **trước** wireframe
- [ ] **State matrix không còn ô `?`**
- [ ] Không màn hình mồ côi — mọi `SCR` xuất hiện trong ≥1 flow
- [ ] **Không Lorem Ipsum** — dùng nội dung thật
- [ ] Mỗi màn có dữ liệu đủ 4 trạng thái: đang tải, rỗng, lỗi, có dữ liệu

**Wireflow — đầu ra chính của phase 08:**

- [ ] Mỗi `FLOW` trong `07-05` có **một trang** `wireframes/flow-FLOW-xxx.html`, thứ tự bước khớp `07-05`
- [ ] **Mọi mũi tên có nhãn** — *bấm gì* hoặc *tự chuyển*. Mũi tên trống là bước chuyển chưa nghĩ xong
- [ ] **Mọi nhánh có nhãn điều kiện** — *nếu mã sai 3 lần*, *nếu mất mạng*…
- [ ] **Mọi màn nằm trong ít nhất một luồng**; màn không vào flow nào đã xử qua `08-04` hoặc giải thích được
- [ ] Mục *Trạng thái còn lại* của trang flow phủ hết ô nào của `08-02` chưa xuất hiện ở đường chính và nhánh
- [ ] Một file màn cho **một ô** của `08-02` — không gộp trạng thái, không dùng JS bật tắt trạng thái
- [ ] Trang flow **nhúng** file màn bằng `iframe`, không chép lại nội dung màn
- [ ] Tên file đúng quy ước `SCR-xxx_ST-xxx_ten.html`, **mã ba chữ số**
- [ ] Mọi file màn có khối `.w-notes` đủ sáu mục, **không mục nào để trống**, có ghi **đường thoát**
- [ ] **Nút không có `href`, không có JavaScript** — điều hướng nằm ở mũi tên trên trang flow
- [ ] **Không chú thích khoảng cách, cỡ chữ, độ cao, màu** trong wireframe — đó là phase 12
- [ ] Mọi file dùng `wireframes/_wireframe.css`; **không màu thương hiệu, không font khác, không ảnh thật**
- [ ] `wireframes/index.html` liệt kê **mọi luồng** và **mọi màn**
- [ ] Đã mở bằng trình duyệt và **đi hết một luồng bằng mắt** từ đầu tới cuối
- [ ] Đã ghi số bước đường chính của luồng cốt lõi, và trả lời **có bước nào bỏ được** hay không
- [ ] **`python .claude/scripts/check_build.py --wireframes wireframes/` báo 0 lỗi**, kết quả dán nguyên vào `08-03` mục 5
- [ ] Màn hình phát sinh trong lúc làm flow đã đi qua `08-04_MISSING_SCREEN_REPORT.md`

## G8 — Growth và đo lường đã duyệt · sau phase 09–10

- [ ] Mỗi thí nghiệm có **target** và **kill rule** đặt trước
- [ ] **Đủ các trạng thái giao dịch**: thành công, thất bại, đang chờ, huỷ giữa chừng, hoàn tiền, hết hạn, gia hạn thất bại, khôi phục mua hàng
- [ ] **Không dark pattern** — không gây hiểu nhầm về giá, thời hạn, cách huỷ
- [ ] Copy deck **phủ hết** `SCR` và `ST`, không còn placeholder
- [ ] Mỗi chuỗi văn bản có **giới hạn ký tự**
- [ ] **Mọi `KPI` tính được từ ≥1 `EVT`**
- [ ] **Mọi `EVT` phục vụ ≥1 `KPI` hoặc bước phễu**
- [ ] Giá viết bằng số **chỉ ở** `09-02`, các file khác trích `PLN-xxx`

## G9 — Sẵn sàng dựng UI · sau phase 11

- [ ] Mọi finding **Critical** đã sửa, hoặc có `DEC` quyết định không sửa kèm lý do
- [ ] Mọi finding usability mức **0 hoặc 1** đã sửa hoặc có `DEC`
- [ ] Báo cáo mồ côi ở `_INDEX.md` mục 5 **rỗng**
- [ ] `11-03_PRE_HANDOVER_FIX_LIST.md` không còn mục đang mở

## G10 — Hướng thị giác đã chốt và prototype đã dựng · sau phase 12

**Phần UI research — `12-00`, phải xong trước khi dựng frame nào:**

- [ ] `12-00` (Nghiên cứu UI) có `status: approved` **trước** khi `12-01` bắt đầu
- [ ] Mục 0 của `12-00` điền trước khi mô tả ảnh — số màn, nội dung nặng nhất, chuỗi chữ dài nhất ở `09-06`, cảm giác người dùng cần có
- [ ] Moodboard đạt nghiệm thu: ≥30 ảnh, ≥3 nguồn, phủ cả 4 chủ đề, **`khong-thich/` có ≥3 ảnh**
- [ ] Mọi `UIP` có quyết định Áp dụng / Điều chỉnh / Không dùng — **không `UIP` nào lấy lý do "vì đẹp" hay "vì đang là trend"**
- [ ] Đã đưa **ba** hướng thiết kế khác nhau thật, đã chọn một, có `DEC`, và ghi vì sao loại hai hướng còn lại
- [ ] Mọi cặp màu chữ trên nền đã kiểm tương phản, **kể cả chữ phụ**; đã trả lời chế độ tối làm hay không
- [ ] Đã quét lần hai ảnh đối thủ theo từng chức năng, **chỉ với chức năng có trong `08-01`**, và nêu chức năng nào không có ảnh tham chiếu
- [ ] Bảng lọc màn hình không chứa `SCR` lạ; số màn "Chốt trước" ≤5 hoặc có lý do; mọi màn "Chốt trước" đã có wireframe ở `08-03`
- [ ] Nhánh dựng đã **hỏi người dùng** và đã chốt kèm `DEC` — nhánh A (Pencil + Agent) không có `DEC` là vi phạm
- [ ] Có hệ thiết kế sẵn: bảng phủ `design-system/_MANIFEST.md` mục 4 đã điền, số thành phần phải dựng mới đã ghi

**Phần dựng — `12-01` đến `12-03`:**

- [ ] `12-01` mục 4 chia thành **lô theo `FLOW`**, mỗi lô có điểm dừng nghiệm thu — không dựng cả bộ một lượt
- [ ] Mọi lô đã ở trạng thái **đã nghiệm thu**
- [ ] **`python .claude/scripts/check_build.py --frames <file>` chạy sạch: 0 lỗi.** Kết quả dán nguyên vào `12-03`, không tóm tắt
- [ ] **Mọi frame bắt buộc đã dựng**
- [ ] **Tên frame khớp mã** `SCR` và `ST`, **ba chữ số** như `08-02`
- [ ] Không còn Lorem Ipsum trong Figma
- [ ] Mọi sai lệch phát hiện lúc dựng đã **cập nhật ngược** vào `08-01`, `08-02`, `09-06`
- [ ] Baseline tiếp cận đã kiểm: tương phản ≥4.5:1, vùng chạm ≥44pt, layout chịu được cỡ chữ lớn nhất, màu không phải kênh truyền tin duy nhất

## G11 — Sẵn sàng bàn giao · sau phase 13

- [ ] Mọi file `Bắt buộc` theo profile có `status: approved`
- [ ] **Không còn `DQ` mở đang chặn**
- [ ] Bảng mục lục gói bàn giao ghi **phiên bản từng file**
- [ ] Mọi `[ASM]` còn sống đã liệt kê tường minh trong `13-01`
- [ ] Mọi `FR` có ít nhất một mục nghiệm thu trong `13-04`
- [ ] Ranh giới trách nhiệm PO / Designer / Dev đã ghi thành bảng
- [ ] `13-01` mục 6 có **khối JSON thứ tự thi công** parse được; mọi `FR` Must và mọi `SCR` ở đúng một đơn vị; `depends_on` không có vòng
- [ ] Bảng **Affordance nằm trên màn của đơn vị khác** đã điền, hoặc ghi rõ không có trường hợp nào
- [ ] Đơn vị chứa hạng mục *Không được cắt* của `05-01` mục 11 đã gắn `must_not_cut: true`
