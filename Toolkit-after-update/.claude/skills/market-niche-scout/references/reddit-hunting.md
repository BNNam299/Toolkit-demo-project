<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : app-opportunity-scout.skill  →  references/reddit-hunting.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Reddit Pain Hunting — Săn nỗi đau để sinh ý tưởng

Tư duy gốc: **đi tìm nỗi đau, không tìm "product ideas"**. Người dùng Reddit không lên để bán ý tưởng — họ lên để **than phiền, tìm giải pháp, hoặc chia sẻ quy trình làm việc**. Ý tưởng nằm trong ba thứ đó.

Reference này là bản đào sâu của Nguồn 2 trong `mining-playbook.md`. Dùng ở Bước 2 (problem mining) của quy trình scout; mọi finding vẫn ghi về format 10 trường và đổ vào need clusters như thường.

## Cách search

- Cụm từ để trong **dấu ngoặc kép ""** trên thanh tìm kiếm Reddit để khớp chính xác.
- Hoặc qua Google với cú pháp: `site:reddit.com "từ_khóa"`.
- Trong subreddit: lọc bài theo **Top (Past Month / Past Year)** để thấy vấn đề được upvote nhiều nhất — upvote là phiếu bầu độ đau.

## Ba bộ từ khóa săn nỗi đau

### Nhóm 1 — Ức chế với công cụ hiện tại (cơ hội làm sản phẩm thay thế / ngách hơn)
| Query | Tín hiệu cơ hội |
|---|---|
| "is there an alternative to" | User chủ động muốn rời sản phẩm đang dùng |
| "disappointed with" | Kỳ vọng bị phản bội — đọc kỹ họ kỳ vọng gì |
| "too expensive" | Cơ hội bản giá rẻ hơn / free tier rộng hơn |
| "bloated with features" | Cơ hội bản tối giản / clean UI |
| "ruined the app" | Thường bùng sau khi app lớn update UI/UX tệ — **cửa sổ thời gian vàng để đón user di cư** |

### Nhóm 2 — Nhu cầu chưa được đáp ứng (cơ hội tính năng / sản phẩm mới)
| Query | Tín hiệu |
|---|---|
| "is there an app for" / "is there a tool that" | Nhu cầu mô tả rõ, đang tìm mà chưa thấy |
| "wish there was a" | Nhu cầu tự phát, chưa ai giải |
| "does anyone know a way to" | Đang tìm workaround — đọc các câu trả lời để thấy workaround hiện tại |
| "how to automate" | Cơ hội tool/SaaS/extension — việc lặp lại đủ nhiều để muốn tự động hóa |

### Nhóm 3 — Quy trình thủ công tốn thời gian (cơ hội tối ưu hóa)
| Query | Tín hiệu |
|---|---|
| "every day I have to" | Tần suất hàng ngày = Frequency 5/5 trong Need Score |
| "spending hours doing" | Workaround cost cao — định giá được thời gian mất |
| "hate doing this manually" | Độ đau cảm xúc cao + hành vi lặp lại |

Nhóm 3 khớp thẳng với "tín hiệu mạnh nhất" trong scoring-validation.md (spreadsheet, copy thủ công, workaround phức tạp) — thấy là nhân đôi sự chú ý.

## Subreddit chiến lược để nằm vùng

### Nhóm "Xin ý tưởng & Than phiền"
- **r/somebodymakethis (SMT)** — người dùng trực tiếp đăng "ai đó làm cái này đi": có nhu cầu nhưng không biết code. Đọc số upvote + comment "tôi cũng cần".
- **r/findanapp** — mô tả nhu cầu cụ thể và hỏi app nào đáp ứng chưa. **Thread không có câu trả lời thỏa đáng = khoảng trống thị trường được xác nhận công khai.**
- **r/complaints, r/mildlyinfuriating** — phàn nàn đời sống/công việc; nhiều tool lớn ra đời chỉ để giải một điều bực mình nhỏ nhặt.

### Nhóm "Xây dựng sản phẩm & Khởi nghiệp" (học từ người đi trước)
- **r/SideProject** — dev đăng MVP vừa build: đọc COMMENT xem user chê gì (UX tệ, thiếu tính năng nào) → mình làm tốt hơn; đồng thời thấy ai đang build gì trong cluster mình theo dõi.
- **r/saas, r/IndieHackers** — thảo luận sâu về tìm ngách, validation, pricing.

## Công thức Niche Down (từ khóa × ngách)

Khi nhắm một tệp khách hàng cụ thể:

```
site:reddit.com/r/<subreddit_ngách> "<từ khóa săn nỗi đau>"
```

Ví dụ chuẩn:
- `site:reddit.com/r/editors "is there a tool"` → công cụ video editor đang mòn mỏi tìm.
- `site:reddit.com/r/FigmaDesign "hate"` → điểm ức chế của designer khi dùng Figma (cơ hội plugin/widget).
- `site:reddit.com/r/iosprogramming "alternative to"` → tool bổ trợ dev iOS đang bất mãn với option hiện tại.

Áp cho các vùng lợi thế của team: `r/ios "storage full"`, `r/GetStudying "focus app"`, `r/learntodraw "don't know what to draw"`, `r/hometheater "universal remote"`, `r/productivity "screen time"`.

## Kỷ luật ghi nhận (giữ nguyên chuẩn scout)

Với mỗi thread giá trị, ghi đủ format 10 trường — đặc biệt: **hoàn cảnh nói ra** (nội dung post) · **đã thử giải pháp nào** (đọc hết comment, đây là bản đồ workaround) · **có trả tiền/mất thời gian cho workaround không** · Evidence = link thread + số upvote + ngày. Đếm upvote và comment "same here" như tín hiệu tần suất, nhưng nhớ quy tắc scout: một thread viral đơn lẻ = trend bề mặt; nhiều thread độc lập cùng nỗi đau = demand thật.
