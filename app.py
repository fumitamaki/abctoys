from flask import Flask, render_template

app = Flask(__name__)

COMPANY = {
    "name": "ABCトイズ株式会社",
    "name_en": "ABC Toys Co., Ltd.",
    "tagline": "わくわくを、カタチに。",
}

PAGES = [
    {"endpoint": "home", "label": "Home"},
    {"endpoint": "about", "label": "About"},
    {"endpoint": "products", "label": "Products"},
    {"endpoint": "brands", "label": "Brands"},
    {"endpoint": "stores", "label": "Stores"},
    {"endpoint": "contact", "label": "Contact"},
]

@app.context_processor
def inject_common_values():
    return {"company": COMPANY, "pages": PAGES}

@app.route("/")
def home():
    stats = [
        {"value": "120+", "label": "Original toy ideas"},
        {"value": "35", "label": "Partner stores"},
        {"value": "4", "label": "Product categories"},
    ]
    news = [
        {"date": "2026.05", "title": "木製知育玩具シリーズ「ABC Blocks」に新ラインアップを追加しました。"},
        {"date": "2026.04", "title": "初夏のファミリー向けイベント展示を開始しました。"},
        {"date": "2026.03", "title": "ぬいぐるみシリーズ「Mori Friends」の特設コーナーを公開しました。"},
    ]
    return render_template("index.html", title="Home", stats=stats, news=news)

@app.route("/about")
def about():
    values = [
        {"title": "Safety", "text": "小さなお子さまにも安心して楽しんでいただける品質を大切にしています。"},
        {"title": "Creativity", "text": "遊びながら想像力が広がる、親しみやすいデザインを追求しています。"},
        {"title": "Sustainability", "text": "長く愛される玩具づくりと、素材やパッケージへの配慮を心がけています。"},
    ]
    return render_template("about.html", title="About", values=values)

@app.route("/products")
def products():
    items = [
        {"title": "ABC Blocks", "text": "色、形、数に親しめる木製ブロックの知育玩具シリーズです。"},
        {"title": "Mori Friends", "text": "やさしい手ざわりと表情にこだわった、ぬいぐるみシリーズです。"},
        {"title": "Tiny Wheels", "text": "街や乗りものへの興味を広げる、ミニカー・乗りもの玩具シリーズです。"},
    ]
    return render_template("products.html", title="Products", items=items)

@app.route("/brands")
def brands():
    steps = [
        "子どもの発達段階や遊び方を観察する",
        "親子で楽しめるテーマとデザインを企画する",
        "安全性と扱いやすさを確認しながら試作する",
        "店頭やオンラインで魅力が伝わる形に整える",
    ]
    return render_template("brands.html", title="Brands", steps=steps)

@app.route("/stores")
def stores():
    cases = [
        {"name": "Seasonal Toy Display", "tag": "Showroom", "summary": "季節のおすすめ商品を組み合わせた、明るく見やすい展示コーナーです。"},
        {"name": "Family Play Corner", "tag": "Event", "summary": "親子で実際に手に取って遊べる、体験型の小さなイベントスペースです。"},
        {"name": "Gift Selection", "tag": "Retail", "summary": "誕生日や入園祝いなどに選びやすい、ギフト向け商品の提案コーナーです。"},
    ]
    return render_template("stores.html", title="Stores", cases=cases)

@app.route("/contact")
def contact(): return render_template("contact.html", title="Contact")

@app.route("/health")
def health(): return {"status":"ok","service":"abc-toys-corporate-site","company":COMPANY["name"]}

if __name__ == "__main__": app.run(host="0.0.0.0", port=8000)
