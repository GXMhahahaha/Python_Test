src_file = open('QQ图片20190827223317.jpg', 'rb')
target_file = open('copy_file.jpg', 'wb')
target_file.write(src_file.read())

src_file.close()
target_file.close()
