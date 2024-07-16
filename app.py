from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)


@app.route('/eightball', methods=['GET', 'POST'])
def eightball():
    return render_template('8ball.html')

@app.route('/answer')
def answer():
    answer = ["https://cdn.britannica.com/82/191982-050-1DF10DB5/ball.jpg",
              "https://media.licdn.com/dms/image/D5612AQHcFhBft8gQ7g/article-cover_image-shrink_600_2000/0/1680193687650?e=2147483647&v=beta&t=ud3fe0W56tsqJCzbUF3h1rOxiTV06KAf9SUCuFhJ-Y8",
              "https://hornershauntedcorner.com/wp-content/uploads/2022/07/HHD-HHC-Magic8Ball3.jpg",
              "https://www.comptia.org/images/default-source/pioneer-article-images/8-ball-signs-point-to-yes.png",
              "https://preview.free3d.com/img/2022/12/3190256732718761805/ud2n6cdj.jpg",
              "https://ih1.redbubble.net/image.2135427937.4557/ur,pin_large_front,square,600x600.jpg",
              "https://ih1.redbubble.net/image.886839728.2816/st,small,507x507-pad,600x600,f8f8f8.jpg",
              "https://www.comptia.org/images/default-source/Pioneer-Article-Images/8-ball-signs-point-to-yes.png"
              ]
    return render_template('answer.html', answerImg=random.choice(answer))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)