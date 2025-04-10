# CTAI Flask后端接口文档

## 1. 首页接口
- 路由：`/`
- 方法：GET
- 功能：重定向到静态首页
- 返回：重定向到 `static/index.html`

## 2. 文件上传接口
- 路由：`/upload`
- 方法：POST
- 参数：
  - file：DCM格式的CT图像文件
- 功能：
  1. 验证文件格式（仅支持.dcm）
  2. 保存文件到指定目录
  3. 调用AI模型进行图像处理
- 返回：JSON格式
  ```json
  {
    "status": 1,  // 1表示成功，0表示失败
    "image_url": "http://127.0.0.1:5003/tmp/image/{pid}",  // 原始图像URL
    "draw_url": "http://127.0.0.1:5003/tmp/draw/{pid}",   // 处理后图像URL
    "image_info": {}  // 图像特征信息
  }
  ```

## 3. 文件下载接口
- 路由：`/download`
- 方法：GET
- 功能：下载指定文件
- 返回：
  - 文件：testfile.zip
  - 类型：application/octet-stream

## 4. 图像显示接口
- 路由：`/tmp/<path:file>`
- 方法：GET
- 参数：
  - file：图像文件路径
- 功能：读取并显示处理后的图像
- 返回：
  - 数据：图像二进制数据
  - 类型：image/png

## 目录结构
```
- uploads/     # 直接上传目录
- tmp/
  - ct/        # dcm文件副本目录
  - image/     # dcm转png目录
  - mask/      # 预测结果掩膜目录
  - draw/      # 勾画肿瘤结果目录
```