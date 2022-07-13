from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route("/index")
def index():
    return render_template("index.html")

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route("/")
@my_view.route('/t5c')
def t5c():
    return render_template("t5c.html") 
    # // redirect 
@my_view.route('/top5car')
def top5car_redirect():
    return redirect(url_for("my_view.t5c"))

@my_view.route('/gallery')
def gallery():
    return render_template("gallery.html") 
    # // redirect 
@my_view.route('/gallery')
def gallery1_redirect():
    return redirect(url_for("my_view.gallery"))

@my_view.route('/news')
def news():
    return render_template("news.html") 
    # // redirect 
@my_view.route('/Membership')
def news_redirect():
    return redirect(url_for("my_view.news"))

@my_view.route('/contact')
def contact():
    return render_template("contact.html") 
    # // redirect 
@my_view.route('/contact us')
def contact_redirect():
    return redirect(url_for("my_view.contact"))


@my_view.route('/about')
def about():
    return render_template("about.html") 
    # // redirect 
@my_view.route('/about')
def about_redirect():
    return redirect(url_for("my_view.about"))


@my_view.route('/suv')
def suv():
    return render_template("suv.html") 
    # // redirect 
@my_view.route('/1')
def suv_redirect():
    return redirect(url_for("my_view.suv"))

@my_view.route('/coupe')
def coupe():
    return render_template("coupe.html")
    # // redirect 
@my_view.route('/2')
def coupe_redirect():
    return redirect(url_for("my_view.coupe")) 

@my_view.route('/city')
def city():
    return render_template("city.html") 
# // redirect 
@my_view.route('/3')
def city_redirect():
    return redirect(url_for("my_view.city"))

@my_view.route('/hatchback')
def hatchback():
    return render_template("hatchback.html") 
# // redirect 
@my_view.route('/4')
def hatchback_redirect():
    return redirect(url_for("my_view.hatchback"))

@my_view.route('/saloon')
def saloon():
    return render_template("saloon.html") 
# // redirect 
@my_view.route('/5')
def saloon_redirect():
    return redirect(url_for("my_view.saloon"))



@my_view.route('/admin')
def admin():
    return render_template("admin.html") 
# // redirect 
@my_view.route('/administrator')
def admin_redirect():
    return redirect(url_for("my_view.admin"))



# @my_view.route('/javascript')
# @my_view.route('/js')
@my_view.route('/home')
def indx_redirect():
    return redirect(url_for("my_view.index"))

# @my_view.errorhandler(404)
# def not_found():
    #  return render_template("404.html")