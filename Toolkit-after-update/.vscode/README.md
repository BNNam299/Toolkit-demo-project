# .vscode — cấu hình sẵn

Thư mục này đã được cấu hình cho việc đọc và viết tài liệu. Không cần sửa gì.

## Đã bật sẵn

`settings.json` bật xuống dòng tự động cho markdown (dòng dài không bị tràn ngang), tăng cỡ chữ và
giãn dòng cho khung preview, bật file nesting cho cây thư mục gọn hơn, và **loại `references/` của skill
khỏi kết quả tìm kiếm** — nếu không thì mỗi lần bạn tìm một mã ID sẽ lẫn hàng trăm dòng từ tài liệu
phương pháp.

`extensions.json` gợi ý năm extension. VS Code sẽ hỏi khi bạn mở thư mục lần đầu.

| Extension | Vì sao cần cho bộ này |
| --- | --- |
| `anthropic.claude-code` | tích hợp Claude Code, xem diff trong IDE |
| `yzhang.markdown-all-in-one` | preview, phím tắt, mục lục tự động |
| `bierner.markdown-mermaid` | **xem được sơ đồ Mermaid** trong `07-05_UX_FLOWS` và `07-03_SITEMAP` |
| `davidanson.vscode-markdownlint` | bắt lỗi định dạng markdown |
| `redhat.vscode-yaml` | kiểm khối front-matter 13 trường ở đầu mỗi tài liệu |

Thiếu `bierner.markdown-mermaid` thì sơ đồ UX flow sẽ hiện ra dạng khối chữ thay vì hình vẽ.
