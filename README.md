# okex-py
OKEx数字货币自动交易python语言SDK (非官方)  
OKEx Cryptocurrency Exchange python SDK (Unofficial)

本项目基于V5 API，支持WebSocket接口  
This project supports V5 REST and WebSocket API.

Python >= 3.10

## 使用例子 Example
``` python3
import okex.v5.account_api as account
import okex.v5.market_api as market
accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False, test=test)
result = accountAPI.get_positions()
# print my positions
print(result)
```

## 文档 Documentation
施工中

## 安装 Installation

### 方法一(Method 1)：
1. 直接安装，Install the package
```
pip install git+https://github.com/quantmew/okex-py.git 
```

### 方法二(Method 2)：
1. 克隆本仓库，Clone the repository
```
git clone https://github.com/quantmew/okex-py.git
```

2. 安装，Install the package
```
cd okex-py
pip install .
```

## 免责声明 Disclaimers
API接口尚不稳定  
API is not yet stable  
本项目不对软件运行的行为做任何保证，对于因使用本软件产生的损失均不承担任何责任。请充分测试软件后再酌情使用。  
This project does not guarantee the behavior of the software and is not responsible for any damages arising from the use of the software. Please test the software sufficiently before using it.  

## 捐助 Donation
如果您觉得这个项目有价值的话，可以通过捐助帮助我们更好地维护这个项目。  
If you think this project is valuable, you can donate to us for better maintainments.   
ETH Address: 0x4E59baf24bB6e7E8b935A32B33b6E6b8Abd67a2a   

