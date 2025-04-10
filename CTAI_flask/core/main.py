from core import process, predict, get_feature


def c_main(path,model):
    image_data = process.pre_process(path)  # 保存png格式图像，得到处理的ROI区域
    # print(image_data)
    predict.predict(image_data,model)  # 预测，保存二值化的mask图像
    process.last_process(image_data[1])  # 将AI预测的病变区域绿色轮廓的形式叠加到原始CT图像上
    image_info = get_feature.main(image_data[1])

    return image_data[1] + '.png', image_info


if __name__ == '__main__':
    pass
