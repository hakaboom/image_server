# 安装步骤

- 由于paddle安装时会影响opencv的版本,导致部分api无法访问,暂时没想到什么好办法,所以该项目手动安装模块

## 确认环境
- 确认python的版本是否满足要求（3.6/3.7/3.8/3.9)
```bash
python --version
```

## 1. 安装Paddle
根据自己的环境可以安装cpu或gpu版本。详细的安装步骤可以去[paddle官网](https://www.paddlepaddle.org.cn/install/quick) 查看
```bash
pip install paddlepaddle==2.2.1
```

## 2. 安装PaddleOcr
```bash
pip install paddleocr>=2.0.1
```
- 安装完成后,卸载已安装的opencv-python与opencv-contrib-python或者升级/自己编译两个opencv库(**版本>4.5.4**)

## 3. 安装py-image-registration
```bash
pip install py-image-registration>=1.0.16
```

## 4. 安装fastapi与uvicorn
```bash
pip install fastapi>=0.70.1
pip install uvicorn[standard]
```