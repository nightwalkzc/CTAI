# CTAI Web 前端项目文档

## 项目概述
CTAI Web是一个基于深度学习的肿瘤辅助诊断系统的前端部分，为医生提供便捷的CT图像上传、肿瘤区域可视化和特征分析功能。系统通过直观的Web界面，帮助医生快速获取肿瘤区域的特征数据，提高诊断效率。

## 技术栈
- Vue.js：前端框架
- Element UI：UI组件库
- ECharts：数据可视化图表库
- Axios：HTTP请求库
- Vue Router：路由管理

## 项目结构
```
CTAI_web/
├── src/                # 源代码目录
│   ├── assets/         # 静态资源
│   ├── components/     # Vue组件
│   │   ├── Header.vue  # 头部组件
│   │   ├── Content.vue # 主要内容组件
│   │   └── Footer.vue  # 底部组件
│   ├── theme/          # 主题相关文件
│   ├── App.vue         # 根组件
│   └── main.js         # 入口文件
├── public/             # 公共资源目录
└── package.json        # 项目配置文件
```

## 核心组件说明

### App.vue
根组件，负责组织整体页面结构，包含Header、Content和Footer三个主要组件。

### Header.vue
页面头部组件，展示系统标题和导航菜单。
- 特点：响应式设计，优雅的标题样式
- 主要功能：系统导航

### Content.vue
系统的核心组件，实现了以下主要功能：
1. CT图像上传与预览
   - 支持文件选择和拖拽上传
   - 实时预览上传的CT图像
   
2. 诊断步骤引导
   - 清晰的步骤展示
   - 包含下载测试文件、上传CT图像、获取分析结果等步骤
   
3. 肿瘤区域展示
   - 并排显示原始CT图像和标注后的图像
   - 支持图像放大预览
   
4. 特征值展示
   - 使用表格展示肿瘤区域的特征数据
   - 支持数据的可视化展示

## 路由配置
项目使用Vue Router进行路由管理，主要路由配置如下：
```javascript
const router = new VueRouter({
    routes: [
        {path: "/App", component: App, meta: {title: "肿瘤辅助诊断系统"}}
    ],
    mode: "history"
})
```

## 状态管理
组件间的数据通信主要通过Props和Events实现，主要状态包括：
- 图像上传状态
- 处理进度
- 分析结果数据

## 使用说明
1. 安装依赖
```bash
npm install
```

2. 开发环境运行
```bash
npm run serve
```

3. 生产环境构建
```bash
npm run build
```

## 开发注意事项
1. 图像处理相关
   - 支持的图像格式：CT图像文件
   - 上传大小限制：根据服务器配置调整
   
2. 性能优化
   - 图像预加载
   - 分批加载大量数据
   - 合理使用缓存

## 部署说明
1. 构建项目生成dist目录
2. 将dist目录下的文件部署到Web服务器
3. 配置服务器支持HTML5 History模式

## 后续优化建议
1. 添加用户认证功能
2. 优化图像处理性能
3. 增加数据导出功能
4. 添加更多可视化图表
5. 优化移动端适配