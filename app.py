from flask import Flask, render_template

app = Flask(__name__)

COMPANY = {
    "name": "株式会社ABCトイズ",
    "name_en": "ABC Toys Co., Ltd.",
    "tagline": "わくわくを、カタチに。",
}

PAGES = [
    {"endpoint": "home", "label": "Home"},
    {"endpoint": "about", "label": "About"},
    {"endpoint": "services", "label": "Services"},
    {"endpoint": "solutions", "label": "Solutions"},
    {"endpoint": "cases", "label": "Cases"},
    {"endpoint": "contact", "label": "Contact"},
]

@app.context_processor
def inject_common_values():
    return {
        "company": COMPANY,
        "pages": PAGES,
    }

@app.route("/")
def home():
    stats = [
        {"value": "99.9%", "label": "Service availability demo"},
        {"value": "4 pages+", "label": "Multi-page navigation"},
        {"value": "GitHub", "label": "Single deployment source"},
    ]
    news = [
        {"date": "2026.05", "title": "新商品キャンペーンサイトのデモを公開しました。"},
        {"date": "2026.04", "title": "社内向け販売ダッシュボードのサンプルを追加しました。"},
        {"date": "2026.03", "title": "Azure App Service 研修用テンプレートを更新しました。"},
    ]
    return render_template("index.html", title="Home", stats=stats, news=news)

@app.route("/about")
def about():
    values = [
        {"title": "Safety", "text": "安全性と品質を重視した商品づくりを想定したダミー説明です。"},
        {"title": "Creativity", "text": "子どもたちの想像力を育む商品企画を想定したダミー説明です。"},
        {"title": "Technology", "text": "Web、データ、クラウドを活用する企業像を想定したダミー説明です。"},
    ]
    return render_template("about.html", title="About", values=values)

@app.route("/services")
def services():
    items = [
        {
            "title": "Toy Store Platform",
            "text": "店舗・EC・キャンペーンサイトを想定した、玩具メーカー向けのダミーサービス紹介です。"
        },
        {
            "title": "Product Campaign Site",
            "text": "新商品や季節キャンペーンの告知ページを想定した、Azure App Service デモ用コンテンツです。"
        },
        {
            "title": "Sales Data Experience",
            "text": "販売状況、在庫、問い合わせ傾向などの可視化を想定したダミーセクションです。"
        },
    ]
    return render_template("services.html", title="Services", items=items)

@app.route("/solutions")
def solutions():
    roadmap = [
        "GitHub リポジトリにアプリケーションコードを配置する",
        "Azure App Service を Python ランタイムで作成する",
        "GitHub から単発デプロイ、または取得後に ZIP デプロイする",
        "ログストリーム、アプリ設定、ヘルスチェックを確認する",
    ]
    return render_template("solutions.html", title="Solutions", roadmap=roadmap)

@app.route("/cases")
def cases():
    cases = [
        {
            "name": "Toy Store Portal Modernization",
            "tag": "Web App",
            "summary": "玩具販売ポータルをクラウドホスティングへ移行した、という想定のダミー事例です。"
        },
        {
            "name": "Sales Dashboard Launch",
            "tag": "Analytics",
            "summary": "店舗別売上や商品カテゴリ別分析を行う社内ダッシュボードを想定しています。"
        },
        {
            "name": "Inventory Automation Starter Kit",
            "tag": "Workflow",
            "summary": "在庫確認や商品問い合わせ対応の効率化を想定したダミー事例です。"
        },
    ]
    return render_template("cases.html", title="Cases", cases=cases)

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/health")
def health():
    return {
        "status": "ok",
        "service": "abc-toys-app-service-final",
        "company": COMPANY["name"],
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
