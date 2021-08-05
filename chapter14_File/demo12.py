with open('QQ图片20190827223317.jpg', mode='rb') as src_file:
    with open('test.jpg', mode='wb') as des_file:
        des_file.write(src_file.read())
        