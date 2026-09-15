---
name: ai-research-provenance
description: Quy tắc ghi nguồn khi nghiên cứu web bằng công cụ AI đọc trang thay cho người. Dùng ở phase 01 và 02 khi đào pain point từ store review, Reddit, keyword, hoặc khi tra số liệu đối thủ. Chống việc bản tóm tắt của AI bị ghi thành [FACT], và chống việc một trang bị tính thành hai nguồn.
---

# Ghi nguồn khi AI đọc web thay người

Skill chiều sâu cho phase 01 và 02. Áp dụng bất kể công cụ nào fetch trang — web search tích hợp,
MCP, hay mô hình khác nối vào.

## Vấn đề skill này chống

Khi AI đọc một trang rồi tóm tắt, cái bạn nhận được là **suy luận của mô hình**, không phải dữ kiện trên
trang. Nếu bản tóm tắt đó bị ghi thẳng vào `01-02_PAIN_MINING_LOG.md` với nhãn `[FACT]` thì toàn bộ hệ
thống nhãn của Pipeline v2 mất tác dụng ngay từ tài liệu đầu tiên — và mọi thứ xây trên đó thừa hưởng lỗi.

## Bốn quy tắc

**1. Trích nguyên văn, không trích bản tóm tắt.**
Mỗi dòng `PN-xxx` phải có **câu chữ y như trên trang**, kèm URL đầy đủ và ngày lấy. Nếu chỉ có bản diễn
giải của mô hình thì nhãn là `[HYP]`, không phải `[FACT]`, và phải quay lại lấy nguyên văn trước khi đóng G1.

**2. Một trang là một nguồn.**
`[INSIGHT]` cần ≥2 nguồn **độc lập**. Đọc lại cùng một trang hai lần, hoặc mô hình tổng hợp từ một trang
rồi trình bày thành nhiều điểm, vẫn là **một** nguồn. Ghi rõ số URL khác nhau, không ghi số dòng.

**3. Số liệu bên thứ ba luôn là ước lượng.**
Apple và Google không công bố DAU, doanh thu, retention của app. Mọi con số kiểu đó đến từ công cụ ước
lượng. Ghi **tên công cụ** và chữ **ước tính**. Không có nguồn thì ghi **Không công bố** — đừng để mô hình
sinh ra một con số nghe hợp lý.

**4. Ghi cả nguồn đã đào mà không ra gì.**
Mục 4 của `01-02` tồn tại để lần sau không đào lại. Nó cũng cho biết kết luận dựa trên bao nhiêu nỗ lực
tìm kiếm, chứ không chỉ dựa trên những gì tình cờ tìm thấy.

## Cách yêu cầu khi nhờ AI đọc web

Yêu cầu **nguyên văn kèm link**, đừng yêu cầu tóm tắt:

```
Đọc <URL>. Trả về 5 trích dẫn NGUYÊN VĂN của người dùng phàn nàn về <chủ đề>,
mỗi trích dẫn kèm ngày đăng nếu có. Không tóm tắt, không diễn giải.
Không tìm thấy thì nói không tìm thấy.
```

Câu cuối quan trọng: không mở đường cho việc "không tìm thấy" biến thành "sinh ra cái gì đó nghe hợp lý".

## Kiểm trước khi đóng cổng G1

- Mọi `PN` có URL mở được và trích dẫn nguyên văn?
- Số **URL khác nhau** của mỗi need cluster ≥2?
- Mọi số liệu đối thủ có tên nguồn, hoặc ghi **Không công bố**?
- Mục "nguồn đã đào không ra gì" có nội dung?

Câu nào trả lời không thì G1 chưa đóng được — bằng chứng chưa đủ chứ không phải tài liệu chưa đẹp.
