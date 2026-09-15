# thu-hoach — dùng công cụ khác đi đào dữ liệu thay Claude

Thư mục này phục vụ một quy trình cụ thể ở **phase 01 và 02**: dùng Codex hoặc OpenCode nối KimiBridge để
đi đào dữ liệu thô, còn Claude chỉ nhận về rồi phân tích. Mục đích là tiết kiệm hạn mức Claude cho phần
cần phán đoán.

Phân vai được vì **đi đào là việc đếm được** — đủ dòng chưa, có URL chưa, có nguyên văn chưa. Còn gom cụm
và diễn giải thì không đếm được.

## Bốn file, bốn vai

| File | Ai ghi | Là gì |
| --- | --- | --- |
| `_BRIEF.md` | **Claude**, trước khi tạm dừng | kế hoạch thu hoạch cho dự án này: đào ở đâu, cụm từ nào, định mức bao nhiêu |
| `_PREVIEW.md` | **công cụ đi đào**, mỗi vòng ghi đè | chỉ **dòng mới của vòng này** — để bạn soi nhanh |
| `_DATA.md` | **công cụ đi đào**, **chỉ nối thêm** | file tích luỹ qua các vòng — đây là thứ bạn approve |
| `README.md` | — | file bạn đang đọc |

**`_DATA.md` chỉ được nối thêm, không được viết đè.** Nếu mỗi vòng ghi lại cả file thì những dòng bạn đã
duyệt ở vòng một có thể bị sửa âm thầm ở vòng ba mà không ai thấy. Đây là ràng buộc quan trọng nhất ở đây.

## Sáu bước

**1. Claude hỏi trước khi đào.** Vào đầu phase 01, Claude hỏi bạn: tự nó đào, hay bạn dùng công cụ khác
đào rồi nạp về. Chọn phương án hai thì sang bước 2.

**2. Claude viết `_BRIEF.md` rồi tạm dừng.** Nó đã đọc brief dự án và danh sách bị cấm nên biết lĩnh vực —
nó đề xuất **nguồn cụ thể, cụm từ tìm cụ thể, tên app đối thủ cụ thể**, kèm định mức và điều kiện dừng.
Bạn xem, sửa, rồi nó ghi một dòng vào `docs/_INDEX.md` mục 8 *Sổ đổi công cụ* và **dừng phiên**.

**3. Bạn nối KimiBridge với Codex hoặc OpenCode**, mở đúng thư mục dự án này.

**4. Vòng lặp thu hoạch.** Giao câu lệnh ở mục dưới. Mỗi vòng công cụ đào xong thì:
ghi dòng mới vào `_PREVIEW.md`, nối vào `_DATA.md`, rồi **dừng lại báo bộ đếm** và chờ bạn.
Bạn soi `_PREVIEW.md`, thấy ổn thì gửi thêm link nguồn cho vòng sau. Lặp cho tới khi đủ.

**5. Bạn approve.** Đủ định mức và soi xong thì đổi trạng thái ở đầu `_DATA.md` thành `đã nghiệm thu`.

**6. Quay lại Claude để phân tích.** Câu lệnh ở cuối file này.

## Ranh giới, không thương lượng

| Việc | Ai làm |
| --- | --- |
| Mở trang, **chép nguyên văn**, ghi URL và ngày | công cụ đi đào |
| Ghi lại nguồn đã đào nhưng không ra gì | công cụ đi đào |
| **Cấp mã `PN`, `NC`, `GAP`** | **chỉ Claude** — mã nằm ở `docs/_ID_REGISTRY.md` |
| Gom cụm, gắn `[FACT]` / `[INSIGHT]` | **chỉ Claude** |
| Viết `01-02`, `01-01`, `02-03` | **chỉ Claude** |

**Công cụ đi đào không được ghi bất cứ gì vào `docs/`.** Hai công cụ cùng cấp mã ID là trùng số ngay.

## Câu lệnh giao cho công cụ đi đào

Dán khối này vào Codex hoặc OpenCode sau khi đã nối KimiBridge:

```
Nhiệm vụ: THU THẬP dữ liệu thô. Không viết tài liệu, không phân tích, không kết luận.

Đọc research-raw/thu-hoach/_BRIEF.md trước — đó là kế hoạch đào cho dự án này.
Theo khuôn cột ở research-raw/thu-hoach/_DATA.md.

Mỗi vòng làm đúng bốn việc:
1. Đào theo nguồn được giao trong vòng này.
2. Ghi ĐÈ research-raw/thu-hoach/_PREVIEW.md — chỉ dòng MỚI của vòng này.
3. NỐI THÊM những dòng đó vào cuối bảng trong research-raw/thu-hoach/_DATA.md.
   Tuyệt đối không sửa hay xoá dòng đã có.
4. DỪNG, báo bộ đếm: tổng dòng / định mức, số loại nguồn, số dòng trùng đã bỏ.
   Rồi chờ tôi gửi nguồn cho vòng sau.

Quy tắc từng dòng:
- Trích NGUYÊN VĂN. Không tóm tắt, không diễn giải, không dịch, không sửa chính tả.
- Mỗi lời phàn nàn MỘT dòng. Một review nói ba chuyện thì tách ba dòng, cùng URL.
- Giữ nguyên ngôn ngữ gốc của người viết.
- KHÔNG tự đặt mã ID. Chỉ đánh số thứ tự tiếp theo số đã có trong _DATA.md.
- Mỗi dòng phải có URL đầy đủ mở được và ngày lấy.
- Trước khi thêm, so với dòng đã có trong _DATA.md để không lặp. Báo số dòng đã bỏ vì trùng.
- Nguồn đào mà không ra gì: ghi vào mục 3 của _DATA.md kèm URL. Không bỏ im lặng.
- Không ghi gì vào docs/.
```

## Nghiệm thu mỗi vòng — năm phút, chỉ soi `_PREVIEW.md`

| Kiểm | Đạt khi |
| --- | --- |
| Mở ngẫu nhiên **3 URL** trong vòng này | câu trích **có thật** trên trang đó, đúng từng chữ |
| Quét tìm dòng tổng kết | **không có** dòng kiểu *"nhiều người phàn nàn về tốc độ"* — đó là diễn giải, bỏ |
| Cột ngôn ngữ | còn nguyên tiếng gốc, không bị dịch sang tiếng Việt |
| Bộ đếm công cụ báo | khớp với số dòng thật trong `_PREVIEW.md` |

Soi từng vòng nhỏ thì bắt được; để tới cuối rồi soi 50 dòng một lượt thì bạn sẽ lướt. Đó là lý do có vòng lặp.

## Khi nào là đủ

Định mức mặc định ở `_BRIEF.md`. Mốc thường dùng: **≥50 dòng, ≥3 loại nguồn.**

Con số 50 cao hơn định mức 30 của `01-02` vì Claude sẽ loại bớt dòng trùng, lạc đề và không dùng được khi
gom cụm. Thu 50 để còn 30 dùng được là tỷ lệ thực tế.

Dấu hiệu đủ theo chất chứ không theo số: **hai vòng liên tiếp không ra thêm loại phàn nàn nào mới**, chỉ
lặp lại những thứ đã có. Lúc đó thêm dòng cũng không đổi kết luận.

## Giao lại cho Claude

```
Dữ liệu thô đã nghiệm thu ở research-raw/thu-hoach/_DATA.md. Đọc hết trước khi làm gì.
Viết 01-02 Sổ đào pain point từ dữ liệu đó: cấp mã PN, gom cụm, gắn nhãn.
Chỉ đào thêm ở chỗ dữ liệu còn hổng, và báo tôi biết hổng ở đâu TRƯỚC khi đào.
Câu người dùng viết nguyên văn thì [FACT]. Kết luận bạn rút từ nhiều dòng thì [INSIGHT].
Ghi một dòng vào docs/_INDEX.md mục 8 là đã quay lại Claude.
```

Câu áp chót là chỗ phân vai đúng: `[FACT]` gắn vào câu người ta viết, `[INSIGHT]` gắn vào kết luận của
Claude. Trộn hai thứ là mất tầng bằng chứng, và không cổng nào bắt được.
