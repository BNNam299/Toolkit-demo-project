<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-persona-journey.skill  →  references/define-toolkit.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Define Toolkit — Chi tiết kỹ thuật & Template

## 5 Whys + Kipling's questions (cách kết hợp chuẩn của team)

**5 Whys**: hỏi "Tại sao?" liên tiếp để xuống **gốc rễ (Root Cause)** thay vì dừng ở triệu chứng. Đa phần một Why có NHIỀU nguyên nhân → đào tiếp từng nhánh cho đến khi còn vài yếu tố cốt lõi khởi nguồn nhiều hệ quả.

**Kipling's (Why-What-Where-When-Who-How)**: sau khi Why được trả lời, các câu sau bám vào đối tượng đó:
> Why: Tại sao mình chưa đi tới X? — Vì không có phương tiện
> → What: phương tiện cần là cái nào? · Where: lấy ở đâu? · Who: ai giúp lấy? · How: lấy bằng cách nào?

**Kết hợp**: 5 Whys trước tìm nguyên nhân cốt lõi → Kipling's để thu thập yếu tố liên quan trong TỪNG nguyên nhân (toàn diện về không gian, thời gian, con người, cách thức). Luôn bắt đầu chuỗi bằng Why, bám sát từ khóa của vấn đề.

## Fishbone Diagram (kết hợp với bộ trên)

- Mỗi **đầu xương cá** = 1 nguyên nhân (cause) tìm ra nhờ 5 Whys (vd: People, Product, Place…)
- Trên **từng nhánh xương** = các yếu tố Kipling's (vd: Not trained, Too busy)

Trình bày dạng text khi không vẽ được:
```
Vấn đề: <effect>
├── Cause 1 (từ Why #..): 
│   ├── Who: ... · Where: ... · How: ...
├── Cause 2: ...
```

## Lotus Blossom

Vấn đề chính ở **nhụy** trung tâm; các yếu tố liên quan là **cánh hoa** xung quanh. Lấy một cánh đáng đào → đặt làm nhụy của bông mới → sinh cánh mới. (Vd: A = tại sao không bán được hàng? → cánh 2 = quán nằm trong ngõ → B = tại sao quán nằm trong ngõ? → ...) Dùng cả ở Define (đào vấn đề) lẫn Ideate (tỏa ý tưởng).

## Insight & Job to be Done

- **Insight** = sự thật vô tình/tạm ẩn giấu, khó phát hiện, có khả năng tác động đến hành vi và quyết định mua của khách hàng.
- Reframe của giáo trình: *Tìm Insight → tìm **JTBD thực sự ẩn sau** Insight đó* · *Khách mua sản phẩm → khách **thuê** sản phẩm để hoàn thành công việc của họ*.
- Quảng cáo/naming làm sáng tỏ bản chất công việc và giúp người dùng NHẬN RA họ có việc cần làm — tên tính năng nên gọi thẳng job.

## Persona — 6 tiêu chí hoạt động tốt

1. **Phù hợp hoàn cảnh (context)** — điểm cụ thể nào của hoàn cảnh kết nối với cách họ dùng sản phẩm bây giờ?
2. **Phản ánh hành vi thực (real)** — thái độ, kỹ năng, động cơ, mục tiêu thật trong miền sản phẩm
3. **Có mục tiêu sau cùng (end-goals)** — muốn đạt điều gì? tính năng nào giúp tốt nhất?
4. **Tình huống thực tế, viết từ persona's perspective** — hình dung cách họ nhận thấy mình sẽ dùng sản phẩm để đạt mục tiêu cụ thể
5. **Bối cảnh rõ ràng** — cách tiếp cận hàng ngày: gặp gì, trong môi trường nào?
6. **Pain points rõ** — điểm khó khăn nhất trong hoàn cảnh của họ là gì?

### Template Persona
```markdown
## Persona: <Tên> — <một dòng định vị>
- **Nhân khẩu**: tuổi, nghề, nơi sống, tình trạng
- **Context**: bối cảnh hằng ngày liên quan sản phẩm
- **Goals (end-goals)**: <kết quả cuối họ muốn>
- **Behaviors thực tế**: thói quen, kỹ năng, thiết bị
- **Pain points**: (kèm quote gốc nếu có)
- **Motivations**: (nối với B=MAT nếu dùng ux-engagement-designer)
- **JTBD**: "Khi <tình huống>, tôi muốn <việc>, để <kết quả>"
- **Nguồn dữ liệu**: <n phỏng vấn, survey..., hoặc [GIẢ ĐỊNH]>
```

## Empathy Map

Says / Thinks / Does / Feels (+ Pains / Gains). Hai thời điểm dùng: (a) trên **người thật** ở bước Define để lọc dữ liệu; (b) **cho Persona** sau khi persona ra đời — đúng trình tự giáo trình.

## Customer Journey Map — Template bảng

| | Awareness | Consideration | Decision | Purchase | Use | Advocacy |
|---|---|---|---|---|---|---|
| **Hành động** | | | | | | |
| **Cảm xúc** (😀/😐/😣) | | | | | | |
| **Chướng ngại vật** | | | | | | |
| **Touchpoint / Kênh** | | | | | | |
| **Động lực** (tại sao cố thực hiện?) | | | | | | |
| — *phần business* — | | | | | | |
| **Mục tiêu DN / Chỉ số** | | | | | | |
| **Hệ thống / Cơ hội** | | | | | | |

Ghi chú vận hành: giai đoạn có thể đổi tên theo sản phẩm (app không bán hàng thì Purchase → Kích hoạt/Onboarding); đánh dấu **khoảnh khắc của sự thật** bằng ⭐; hành trình giả định phải qua vòng xác thực với người dùng thật rồi mới chốt.

## 5 loại CJM — chọn theo mục đích

| Loại | Dùng khi |
|---|---|
| Bản đồ trải nghiệm | Kiểm tra/xác thực giả định; tìm cơ hội thu hút mới hoặc cải thiện hiện tại; dự đoán phản ứng để chủ động phản hồi; gắn success metrics theo giai đoạn |
| Trạng thái hiện tại | Cải thiện liên tục dựa trên quan sát + survey + analytics |
| Trạng thái tương lai | Minh họa tầm nhìn với mục tiêu rõ, dựa trên thực tế hiện tại |
| Cuộc sống hàng ngày | Ghi mọi hoạt động trong ngày của khách (kể cả không liên quan mình) — tìm pain trước cả khi khách biết; tìm khe thời gian sản phẩm chen vào |
| Empathy map | Khi cần lớp cảm xúc sâu cho một persona |
