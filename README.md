### 说明：

* 拉取项目框架：
定义api_model：api接口类型，也就是接口返回结构，请参照api_model下的test.py
定义base_model: 定义基础字段模型，一般与数据库字段同步，请参照base_model下的test.py(最好由一个负责人定义该接口)
controlers：主要是业务处理函数
api.py: 这个graphql数据处理入口，开发者只需要导入api_model里的对象，再调用controlers里面的处理函数即可，请参照例子(最好由一个负责人定义该接口)
lambda_function.py: 该函数是aws serverless 函数入口，这个函数不用动，主要定义好接口好修改函数test_python_grapgql中的event即可
调用（请求方法GET/POST由开发者定义，最好POST）：

固定请求参数
{“query”:”graphql标准语法”,”variables”:”变量”}
python第三库

开发者需要定义requirments.txt并打包https://aws.amazon.com/cn/blogs/china/use-aws-lambda-layer-function/
aws部署API方式文档：https://www.jianshu.com/p/948e7e9848ca
