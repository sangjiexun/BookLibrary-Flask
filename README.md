# 图书馆管理系统

## 项目简介
图书馆管理系统是一个基于Flask框架开发的图书管理平台，提供图书借阅、归还、查询和管理等功能，帮助图书馆实现数字化管理，提高服务效率。

## 技术架构

### 后端技术
- **Flask**: Python Web框架
- **Flask-SQLAlchemy**: ORM数据库工具
- **Flask-Login**: 用户认证管理
- **Flask-WTF**: 表单处理和验证
- **SQLite**: 轻量级数据库

### 前端技术
- **HTML5/CSS3/JavaScript**: 前端基础
- **Jinja2**: 模板引擎
- **Bootstrap**: 响应式UI框架

### 项目结构
```
BookLibrary/
├── app.py                # 主应用文件
├── config.py             # 配置文件
├── models.py             # 数据库模型
├── forms.py              # 表单定义
├── routes.py             # 路由定义
├── templates/
│   ├── base.html         # 基础布局
│   ├── index.html        # 首页
│   ├── login.html        # 登录页面
│   ├── register.html     # 注册页面
│   ├── books.html        # 图书列表
│   ├── book_detail.html  # 图书详情
│   ├── borrow.html       # 借阅页面
│   ├── return.html       # 归还页面
│   └── admin.html        # 管理员页面
└── static/
    ├── css/              # 样式文件
    └── js/               # JavaScript文件
```

## 核心功能

### 用户管理
- 用户注册与登录
- 权限控制（普通用户/管理员）

### 图书管理
- 图书信息管理（添加、编辑、删除）
- 图书分类管理
- 图书状态跟踪

### 借阅管理
- 图书借阅
- 图书归还
- 借阅历史查询
- 逾期提醒

### 搜索与查询
- 图书标题搜索
- 作者搜索
- ISBN搜索
- 分类查询

### 统计分析
- 借阅统计
- 热门图书分析
- 读者活跃度分析

## 数据库模型

### 主要模型
- **User**: 用户信息
- **Book**: 图书信息
- **Category**: 图书分类
- **BorrowRecord**: 借阅记录

## 安装与运行

### 环境要求
- Python 3.6+
- pip包管理器

### 安装步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/sangjiexun/BookLibrary-Flask.git
   cd BookLibrary-Flask
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 初始化数据库
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. 运行应用
   ```bash
   python app.py
   ```

5. 访问应用
   打开浏览器访问 http://localhost:5000

## 配置说明

### 数据库配置
默认使用SQLite数据库，可在`config.py`中修改：

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
```

### 应用配置
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 安全措施
- 密码哈希存储
- CSRF保护
- 权限控制
- 输入验证

## 部署建议
- 使用Gunicorn作为WSGI服务器
- 使用Nginx作为反向代理
- 配置HTTPS
- 数据库定期备份

## 贡献指南
欢迎提交Issue和Pull Request来改进这个项目。

## 许可证
MIT License

---

# Book Library Management System

## Project Introduction
Book Library Management System is a book management platform developed based on the Flask framework, providing book borrowing, returning, querying and management functions to help libraries implement digital management and improve service efficiency.

## Technical Architecture

### Backend Technology
- **Flask**: Python Web framework
- **Flask-SQLAlchemy**: ORM database tool
- **Flask-Login**: User authentication management
- **Flask-WTF**: Form handling and validation
- **SQLite**: Lightweight database

### Frontend Technology
- **HTML5/CSS3/JavaScript**: Frontend basics
- **Jinja2**: Template engine
- **Bootstrap**: Responsive UI framework

### Project Structure
```
BookLibrary/
├── app.py                # Main application file
├── config.py             # Configuration file
├── models.py             # Database models
├── forms.py              # Form definitions
├── routes.py             # Route definitions
├── templates/
│   ├── base.html         # Base layout
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── books.html        # Book list
│   ├── book_detail.html  # Book details
│   ├── borrow.html       # Borrowing page
│   ├── return.html       # Return page
│   └── admin.html        # Admin page
└── static/
    ├── css/              # Style files
    └── js/               # JavaScript files
```

## Core Features

### User Management
- User registration and login
- Permission control (ordinary user/admin)

### Book Management
- Book information management (add, edit, delete)
- Book category management
- Book status tracking

### Borrowing Management
- Book borrowing
- Book returning
- Borrowing history query
- Overdue reminder

### Search and Query
- Book title search
- Author search
- ISBN search
- Category query

### Statistics and Analysis
- Borrowing statistics
- Popular book analysis
- Reader activity analysis

## Database Models

### Main Models
- **User**: User information
- **Book**: Book information
- **Category**: Book category
- **BorrowRecord**: Borrowing record

## Installation and Running

### Environment Requirements
- Python 3.6+
- pip package manager

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/sangjiexun/BookLibrary-Flask.git
   cd BookLibrary-Flask
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Access the application
   Open a browser and visit http://localhost:5000

## Configuration Instructions

### Database Configuration
SQLite is used by default, which can be changed in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
```

### Application Configuration
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Security Measures
- Password hash storage
- CSRF protection
- Permission control
- Input validation

## Deployment Recommendations
- Use Gunicorn as WSGI server
- Use Nginx as reverse proxy
- Configure HTTPS
- Regular database backups

## Contribution Guide
Welcome to submit Issues and Pull Requests to improve this project.

## License
MIT License