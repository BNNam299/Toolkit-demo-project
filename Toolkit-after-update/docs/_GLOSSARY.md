---
doc_id: _GLOSSARY
title: Từ vựng thống nhất
owner: PO
version: 0.1.0
status: draft
---

# _GLOSSARY — Từ vựng

Đây là **nguồn chân lý về cách gọi**. Khi hai tài liệu gọi cùng một thứ bằng hai tên, file này thắng.

Đưa file này cho freelancer **ngay khi bắt đầu**, cùng `05-03_PROJECT_OVERVIEW.md` và `00-02_SCOPE_LOCK.md`.

## Từ vựng sản phẩm

| Thuật ngữ | Định nghĩa | **Không gọi là** | Xuất hiện ở |
| --- | --- | --- | --- |
| | | | |

Cột "không gọi là" quan trọng ngang cột định nghĩa. Nó ngăn việc cùng một màn hình bị gọi là *Trang chủ*,
*Home*, *Dashboard* và *Màn chính* ở bốn tài liệu khác nhau.

## Thuật ngữ giữ nguyên tiếng Anh

Những từ dưới đây dùng nguyên tiếng Anh trong mọi tài liệu, không dịch:

PRD · MVP · onboarding · paywall · trial · subscription · retention · conversion · activation ·
user flow · wireframe · usability · edge case · acceptance criteria · persona · insight · funnel

## Thuật ngữ chuyên môn — nghĩa một câu

**Bảng này là bộ máy, không phải bài đọc thêm.** `validate_docs.py` đọc cột đầu để biết thuật ngữ nào cần
diễn giải; tài liệu nào dùng một thuật ngữ trong bảng mà không liệt kê nó ở mục *Thuật ngữ dùng trong tài
liệu này* thì ra **LỖI**.

Vì sao phải làm vậy: một dự án có Product Owner, Designer và Dev cùng đọc chung một bộ tài liệu. Người viết
nào cũng viết bằng tiếng của nghề mình và tưởng ai cũng hiểu. Designer đọc `NFR` thấy *p95* thì bỏ qua; Dev
đọc `04-04` thấy *JTBD* thì bỏ qua; cả hai vẫn gật đầu duyệt. Chỗ hỏng không nằm ở đoạn khó hiểu — nó nằm ở
chỗ **cả hai bên đều tưởng mình hiểu và không ai hỏi lại**.

Ba luật khi viết cột nghĩa:

1. **Không dùng thuật ngữ khác để giải thích một thuật ngữ.** Giải thích *activation* bằng *conversion* là
   không giải thích gì.
2. **Một câu.** Dài hơn nghĩa là đang viết bài giảng, không phải diễn giải.
3. **Giữ nguyên thuật ngữ trong bài, đừng thay bằng chữ tiếng Việt tự chế.** Người trong nghề cần đúng từ
   đó để tra cứu và để nói chuyện với bên ngoài. Diễn giải là **thêm vào**, không phải **thay thế**.

Thiếu thuật ngữ nào thì thêm dòng vào bảng — bảng này thuộc về dự án, không phải bộ mẫu.

| Thuật ngữ | Nghĩa một câu | Vai trò hay không hiểu |
| --- | --- | --- |
| JTBD | Việc người dùng đang cần làm xong — mô tả theo việc họ muốn xong, không theo tính năng ta định làm | Dev · Designer |
| Pain point | Một chỗ khó chịu cụ thể người dùng gặp, có bằng chứng ai đó thật sự kêu | Dev |
| Need cluster | Nhóm nhiều lời kêu ca khác nhau nhưng thật ra cùng một nhu cầu | Dev · Designer |
| Persona | Bản mô tả một kiểu người dùng, dựng từ dữ liệu thật, dùng để cả nhóm nhắc tới cùng một người | Dev |
| Proto-persona | Persona dựng khi chưa có dữ liệu — là phỏng đoán, phải ghi rõ là phỏng đoán | Dev · Designer |
| Insight | Kết luận rút ra khi ít nhất hai nguồn dữ liệu cùng chỉ về một hướng | Dev |
| Value proposition | Câu trả lời cho "vì sao người ta chọn cái này thay vì cách họ đang làm" | Dev |
| Định vị sản phẩm | Chỗ đứng của sản phẩm so với các lựa chọn khác trong đầu người dùng | Dev |
| MVP | Bản đầu tiên nhỏ nhất vẫn giải quyết trọn vấn đề cho một nhóm người — không phải bản rút gọn qua loa | Designer |
| Scope | Danh sách những gì có làm và không làm trong bản này | Designer |
| Khoá phạm vi | Chốt danh sách không làm, để về sau ai muốn thêm phải mở ra sửa có ghi vết | Dev · Designer |
| Must / Should / Could | Mức ưu tiên: Must là thiếu thì không phát hành được, Should là quan trọng nhưng hoãn được, Could là có thì tốt | Designer |
| Acceptance criteria | Điều kiện cụ thể để nói một yêu cầu đã làm xong — kiểm được bằng thao tác, không tranh cãi | Designer |
| Business rule | Quy tắc tính toán hoặc quy tắc nghiệp vụ của sản phẩm, đúng ở mọi màn hình | Designer |
| Functional requirement | Yêu cầu về việc app phải làm được gì | Designer |
| Non-functional requirement | Yêu cầu về việc app phải làm tốt tới mức nào: nhanh bao nhiêu, chịu được bao nhiêu, hỏng thì sao | Designer · PO |
| Use case | Một lượt người dùng dùng app để xong một việc, kể theo từng bước | Designer |
| Happy path | Đường đi khi mọi thứ suôn sẻ, không lỗi, không thiếu dữ liệu | PO |
| Edge case | Tình huống hiếm nhưng có thật, dễ làm hỏng: mất mạng, dữ liệu rỗng, người dùng bấm hai lần | PO · Designer |
| Truy nguyên | Khả năng đi ngược từ một nút bấm về đúng vấn đề người dùng đã sinh ra nó | Dev · Designer |
| Cổng | Điểm dừng bắt buộc: chưa đủ điều kiện thì không sang chặng sau | Dev · Designer |
| Information architecture | Cách sắp xếp và đặt tên mọi thứ trong app, để người dùng đoán đúng chỗ cần tìm | Dev · PO |
| Sitemap | Sơ đồ cây các màn hình, cho biết màn nào nằm dưới màn nào | Dev |
| User flow | Đường đi qua nhiều màn để xong một việc | Dev |
| Wireframe | Bản vẽ màn hình khi chưa có màu và hình ảnh, để chốt nội dung và bố cục trước | Dev · PO |
| Wireflow | Nhiều wireframe xếp cạnh nhau, nối bằng mũi tên có nhãn, để thấy trọn một đường đi | Dev · PO |
| Screen inventory | Bảng liệt kê đủ mọi màn hình sẽ có, làm trước khi vẽ bất cứ màn nào | Dev · PO |
| State matrix | Bảng liệt kê mọi trạng thái của từng màn: bình thường, đang tải, rỗng, lỗi, mất mạng | Dev · PO |
| Trạng thái | Một dáng vẻ khác của cùng một màn hình khi hoàn cảnh khác — cùng màn nhưng người dùng thấy khác | Dev |
| Empty state | Màn hình khi chưa có dữ liệu gì để hiện, và phải có đường đi tiếp | Dev · PO |
| Affordance | Dấu hiệu thị giác cho người dùng đoán được cái này bấm được hay kéo được | Dev · PO |
| Mental model | Cách người dùng hình dung sản phẩm hoạt động, có thể khác hẳn cách nó thật sự hoạt động | Dev |
| Heuristic | Nguyên tắc kinh nghiệm đã được kiểm chứng, dùng để soi giao diện mà chưa cần test với người dùng | Dev · PO |
| Usability | Mức độ dễ dùng, đo được: xong việc không, mất bao lâu, sai mấy lần | Dev |
| Accessibility | Mức độ dùng được với người khiếm thị, khiếm thính, tay yếu, mắt kém | Dev · PO |
| Vùng chạm | Vùng bấm được của một nút, phải đủ lớn cho ngón tay chứ không chỉ vừa cái icon | PO |
| Thấy ngay không cần cuộn | Phần màn hình người dùng nhìn thấy khi vừa mở, trước khi vuốt | PO · Dev |
| Design system | Bộ thành phần giao diện dùng lại được, có tên thống nhất, để mọi màn nhất quán | Dev · PO |
| Component | Một mảnh giao diện dùng lại nhiều nơi, ví dụ một nút, một thẻ, một hàng danh sách | PO |
| Design token | Giá trị nền tảng đặt tên sẵn — màu, cỡ chữ, khoảng cách — để đổi một chỗ là đổi cả app | PO |
| Lo-fi / hi-fi | Lo-fi là bản thô chỉ có bố cục; hi-fi là bản gần giống app thật, có màu và hình | Dev · PO |
| Prototype | Bản bấm thử được, chưa phải app thật, dùng để test với người dùng trước khi viết code | Dev |
| Moodboard | Tập ảnh tham khảo gom lại để chốt hướng thị giác trước khi thiết kế | Dev · PO |
| Copy deck | Bảng chứa toàn bộ câu chữ sẽ hiện trên app, mỗi câu một mã | Dev |
| Microcopy | Những câu rất ngắn trên giao diện: chữ trên nút, dòng báo lỗi, dòng gợi ý trong ô nhập | Dev |
| Onboarding | Chuỗi màn đầu tiên sau khi cài, dẫn người dùng tới lúc thấy được giá trị | Dev |
| Aha moment | Khoảnh khắc người dùng lần đầu hiểu ra sản phẩm có ích cho mình | Dev |
| Activation | Người dùng đã làm xong hành động chứng tỏ họ nhận được giá trị lần đầu | Dev · Designer |
| Retention | Tỉ lệ người dùng quay lại sau một khoảng thời gian | Dev · Designer |
| Churn | Tỉ lệ người dùng bỏ đi, không quay lại nữa | Dev · Designer |
| Conversion | Tỉ lệ người đi qua được một bước quan trọng, ví dụ từ dùng thử sang trả tiền | Dev · Designer |
| Funnel | Chuỗi bước nối nhau, đếm xem mỗi bước rơi rụng bao nhiêu người | Dev · Designer |
| Paywall | Màn hình chặn lại và mời trả tiền để dùng tiếp | Dev |
| Trial | Khoảng thời gian dùng thử miễn phí trước khi bị tính tiền | Dev |
| Cohort | Nhóm người dùng bắt đầu cùng một mốc thời gian, theo dõi riêng để so sánh | Designer |
| KPI | Chỉ số dùng để biết sản phẩm có đang đi đúng hướng không | Dev · Designer |
| Event | Một hành động của người dùng được app ghi lại để đếm về sau | Designer |
| Event taxonomy | Bộ quy ước đặt tên các event, để số đếm được về sau không loạn | Designer |
| Guardrail metric | Chỉ số canh chừng: không cần tăng, nhưng tụt là phải dừng thử nghiệm | Designer |
| A/B test | Chia người dùng thành hai nhóm thấy hai bản khác nhau, để biết bản nào tốt hơn | Designer |
| Kill rule | Điều kiện chốt trước, chạm tới là dừng thử nghiệm ngay, không bàn thêm | Designer |
| API | Cách hai phần mềm nói chuyện với nhau — bên này hỏi, bên kia trả | PO · Designer |
| On-device | Xử lý ngay trên máy người dùng, không gửi lên máy chủ — thường nhanh hơn và riêng tư hơn | PO · Designer |
| Latency | Độ trễ: từ lúc người dùng bấm tới lúc thấy kết quả | PO · Designer |
| p95 | Con số mà 95 trên 100 lần đo nằm dưới mức đó — dùng thay cho số trung bình vì trung bình giấu mất lần chậm | PO · Designer |
| Cold start | Lần mở app khi nó chưa chạy sẵn trong nền — lần chậm nhất | PO · Designer |
| Cache | Bản lưu tạm để lần sau lấy ra nhanh, không phải hỏi lại máy chủ | PO · Designer |
| Offline-first | Thiết kế để app vẫn dùng được khi mất mạng, đồng bộ lại sau | PO · Designer |
| Permission | Quyền hệ điều hành phải xin người dùng: máy ảnh, thông báo, vị trí, danh sách app | PO |
| Push notification | Thông báo do máy chủ đẩy xuống; khác thông báo do chính máy hẹn giờ tự bắn | PO · Designer |
| SDK | Bộ thư viện của bên thứ ba nhúng vào app để dùng dịch vụ của họ | PO · Designer |
| Feature flag | Công tắc bật tắt một tính năng mà không cần phát hành bản mới | PO · Designer |
| Migration | Việc chuyển dữ liệu cũ sang cấu trúc mới khi app đổi cách lưu | PO · Designer |
| Crash rate | Tỉ lệ phiên dùng bị app tắt đột ngột | PO |
| Rate limit | Giới hạn số lần được gọi tới một dịch vụ trong một khoảng thời gian | PO · Designer |

> Cột cuối là **gợi ý**, không phải phán xét. Nó nhắc người viết rằng câu này sẽ có người đọc mà không có
> nền chuyên môn tương ứng.

## Tra nhanh mã — dùng khi Claude nhắc một mã mà bạn không nhớ nghĩa

Bảng này để **tra**, không phải để đọc hết. Claude có nghĩa vụ tự viết kèm nghĩa mỗi khi nhắc một mã
(xem quy tắc *Gọi tên tường minh* ở `CLAUDE.md`), nên bình thường bạn không cần mở bảng này.

### 61 tài liệu

| doc_id | Nghĩa |
| --- | --- |
| `00-01` | Bản tóm tắt dự án |
| `00-02` | Khoá phạm vi — danh sách bị cấm |
| `01-01` | Thị trường và vùng nhu cầu |
| `01-02` | Sổ đào pain point |
| `02-01` | Bản đồ đối thủ |
| `02-02` | Mổ xẻ đối thủ |
| `02-03` | Đào review người dùng |
| `02-04` | Khoảng trống cơ hội |
| `03-01` | Chấm điểm nhu cầu và cơ hội |
| `03-02` | Các concept ứng viên |
| `03-03` | Kế hoạch kiểm chứng |
| `03-04` | Kết quả kiểm chứng |
| `03-05` | Brief khả thi công nghệ gửi Dev |
| `04-01` | Kế hoạch và bộ câu hỏi nghiên cứu |
| `04-02` | Sổ ghi nghiên cứu |
| `04-03` | Insight người dùng |
| `04-04` | Việc người dùng cần làm xong (JTBD) |
| `04-05` | Chân dung người dùng |
| `04-06` | Hành trình người dùng |
| `04-07` | Audit chất lượng nghiên cứu |
| `04-08` | Bản đồ đồng cảm (Empathy Map) |
| `05-01` | Tài liệu yêu cầu sản phẩm (PRD) |
| `05-02` | Audit PRD |
| `05-03` | Tổng quan dự án cho người mới |
| `06-00` | Brief tính năng gửi Dev nghiên cứu |
| `06-01` | Ca sử dụng |
| `06-02` | Yêu cầu chức năng |
| `06-03` | Yêu cầu phi chức năng |
| `06-04` | Quy tắc nghiệp vụ |
| `06-05` | Nhu cầu quyền và dữ liệu |
| `07-00` | UX Research — mổ xẻ UX/UI/luồng đối thủ từ ảnh |
| `07-01` | Phân tích nhiệm vụ |
| `07-02` | Kiến trúc thông tin |
| `07-03` | Sơ đồ cấu trúc app |
| `07-04` | Bản đồ user story |
| `07-05` | Luồng trải nghiệm người dùng |
| `08-01` | Kiểm kê màn hình |
| `08-02` | Ma trận trạng thái |
| `08-03` | Wireflow — màn nối bằng mũi tên có nhãn |
| `08-04` | Báo cáo màn hình còn thiếu |
| `09-01` | Đặc tả onboarding |
| `09-02` | Đặc tả kiếm tiền và paywall |
| `09-03` | Gắn kết, giữ chân, thông báo |
| `09-04` | Kế hoạch thử nghiệm A/B |
| `09-05` | Giọng điệu thương hiệu |
| `09-06` | Toàn bộ câu chữ trong app |
| `09-07` | Review câu chữ UX |
| `10-01` | Khung chỉ số |
| `10-02` | Danh mục event đo lường |
| `10-03` | Định nghĩa phễu |
| `11-01` | Review thiết kế theo heuristic |
| `11-02` | Đánh giá khả dụng |
| `11-03` | Danh sách phải sửa trước bàn giao |
| `12-00` | Nghiên cứu UI, chốt hướng thị giác |
| `12-01` | Spec để dựng prototype |
| `12-02` | Design system và khả năng tiếp cận |
| `12-03` | Đối chiếu prototype với tài liệu |
| `13-01` | Gói bàn giao |
| `13-02` | Sổ câu hỏi cho Dev |
| `13-03` | Hợp đồng tech-input |
| `13-04` | Bộ tiêu chí nghiệm thu |

### 12 cổng

| Cổng | Nghĩa | Chạy khi nào |
| --- | --- | --- |
| `G0` | Brief đã khoá | sau phase 00 |
| `G1` | Cơ hội có bằng chứng | sau phase 01–02 |
| `G2` | Cơ hội đã kiểm chứng và công nghệ khả thi | sau phase 03 |
| `G3` | Nghiên cứu đã audit | sau phase 04 |
| `G4` | PRD đã duyệt | sau phase 05 |
| `G5` | Yêu cầu đã phân rã | sau phase 06 |
| `G6` | Cấu trúc đã duyệt | sau phase 07 |
| `G7` | Kiểm kê màn hình xong | sau phase 08 |
| `G8` | Growth và đo lường đã duyệt | sau phase 09–10 |
| `G9` | Sẵn sàng dựng UI | sau phase 11 |
| `G10` | Prototype đã dựng | sau phase 12 |
| `G11` | Sẵn sàng bàn giao | sau phase 13 |

### Tiền tố ID

Ý nghĩa từng tiền tố (`FR`, `SCR`, `DEC`, `CAP`…) nằm ở `docs/_ID_REGISTRY.md`, cột **Nghĩa**.
Đó là nguồn chân lý; đừng chép lại sang đây để tránh hai bảng lệch nhau.

## Bảng quy đổi mức ưu tiên — một cách gọi duy nhất

Đây là **nguồn chân lý về mức ưu tiên**. Mọi tài liệu, và cả Dev khi ước lượng, dùng đúng bảng này.
Hai người nói *Must* và *P0* mà không chắc là cùng một thứ thì scope đã lệch mà chưa ai biết.

| Tier | Gọi ở `05-01`, `06-01` | Gọi ở `06-02` | Mã Dev hay dùng | Trong MVP? |
| --- | --- | --- | --- | --- |
| **Tier 1** | Must | Cao | P0 | **Có** |
| **Tier 2** | Should | Trung bình | P1 | Không — Post-MVP |
| **Tier 3** | Could | Thấp | P2 | Không — tương lai |

**Định nghĩa MVP của dự án này:** _liệt kê đúng những `FEAT` và `UC` nằm trong MVP, hoặc ghi
"MVP = toàn bộ N FEAT"._

Mọi trường hợp lệch khỏi bảng này phải ghi vào bảng **Nâng hạ phạm vi** ở `05-01` mục 11, kèm lý do.
Lệch mà không ghi là lỗi, không phải linh hoạt.

## Nhãn trạng thái nội dung

| Nhãn | Nghĩa | Điều kiện được dùng |
| --- | --- | --- |
| `[FACT]` | Dữ kiện | Có nguồn kiểm chứng được |
| `[INSIGHT]` | Kết luận có cơ sở | Từ ≥2 nguồn hoặc ≥3 quan sát độc lập |
| `[HYP]` | Giả thuyết | Có điều kiện bác bỏ rõ ràng |
| `[ASM]` | Giả định tạm | Có dòng ở `_ASSUMPTION_REGISTER.md` |
| `[REC]` | Đề xuất | Kèm lý do và phương án thay thế |
| `[DEC]` | Đã quyết | Có `DEC ID` ở `_DECISION_LOG.md` |
