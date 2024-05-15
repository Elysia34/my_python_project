from flask import Flask, render_template,request, jsonify
import pandas as pd
import json
# 初始化app
# app = Flask(__name__, static_url_path='', template_folder='.', static_folder='.')
app = Flask(__name__)
# 设置响应请求的目录
@app.route('/')
def index():
    return render_template('/job.html')


@app.route('/ajax_get', methods=['GET', 'POST'])
def ajax_data():
    return "这个是来自flask的数据"


@app.route('/get_company', methods=['GET'])
def get_company():
    json = request.json
    print('recv:', json)
    re_data = {
           'company_num': 1001,
           'job_num': 5001,
           'avg_salary': 50001,
    }
    return jsonify(re_data)

@app.route('/get_industry', methods=['GET'])
def get_industry():
    # 读取CSV文件
    # df = pd.read_csv('./csv/data.csv')
    df = pd.read_csv('./csv/data3.csv', encoding="GB2312")
    # 访问特定的列（例如，'Column1'）
    # print(df['industry_type'])
    industry_type_list = df['industry_type']
    industry_type_value_list = df['industry_type_value']

    industry_type_list = industry_type_list.tolist()
    # industry_type_value_list = json.dumps(industry_type_value_list.tolist())
    industry_type_value_list = industry_type_value_list.tolist()
    re_data = {
           # 'industry_type': ["广东", "广东", "广东"],
           'industry_type': industry_type_list,
           'industry_type_value':  industry_type_value_list,
    }
    print(re_data)
    # re_data = {
    #        'industry_type': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    #        'industry_type_value':  [120, 200, 150, 80, 70, 110, 130],
    # }
    return jsonify(re_data)


if __name__ == '__main__':
    app.run() # 启动服务