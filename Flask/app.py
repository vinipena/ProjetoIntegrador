from flask import Flask, render_template, url_for
app = Flask(__name__)

lista_membros =[
                ('Daniele','Estudando de Eng. da Computação','https://www.linkedin.com/in/viniciuspena/','https://media-exp1.licdn.com/dms/image/C4E03AQG05Rms7pFYhA/profile-displayphoto-shrink_200_200/0/1583168044658?e=1640822400&v=beta&t=FJmZoDK8trGfvRRz7qIGKXyT8WeR5Ir9gkqdIiakyDQ'),
                ('Debora','Estudando de Eng. da Computação','https://www.linkedin.com/in/deboracscarvalho/','https://media-exp1.licdn.com/dms/image/C4E03AQGu8zHyf6lReg/profile-displayphoto-shrink_200_200/0/1580772892139?e=1640822400&v=beta&t=KC8omaFz3_d3x6yRlQzqDj_ltIdSLmX8v979h7DbGBE'),
                ('Elizete','Estudando de Eng. da Computação','https://www.linkedin.com/in/elizeteslacerda/','https://media-exp1.licdn.com/dms/image/C4D03AQGPHdUctj3pMw/profile-displayphoto-shrink_200_200/0/1604791383586?e=1640822400&v=beta&t=734AhVxlU_UWe42fzMK2ghruLgToAVmybEQwxLont98'),
                ('Marcio','Estudando de Eng. da Computação','https://www.linkedin.com/in/viniciuspena/','https://media-exp1.licdn.com/dms/image/C4E03AQG05Rms7pFYhA/profile-displayphoto-shrink_200_200/0/1583168044658?e=1640822400&v=beta&t=FJmZoDK8trGfvRRz7qIGKXyT8WeR5Ir9gkqdIiakyDQ'),
                ('Tiago','Estudando de Eng. da Computação','https://www.linkedin.com/in/tiago-vidal-774236215/','https://media-exp1.licdn.com/dms/image/C4E03AQG96c7YMQ8gUg/profile-displayphoto-shrink_200_200/0/1624285170016?e=1640822400&v=beta&t=6xTaZ9K6MNOwHXRQazWpJOca0SNAlt9H6QjhzRlFHSo'),
                ('Vinicius','Estudando de Eng. da Computação','https://www.linkedin.com/in/viniciuspena/','https://media-exp1.licdn.com/dms/image/C4E03AQG05Rms7pFYhA/profile-displayphoto-shrink_200_200/0/1583168044658?e=1640822400&v=beta&t=FJmZoDK8trGfvRRz7qIGKXyT8WeR5Ir9gkqdIiakyDQ')]
@app.route("/")
def hello_world():
    return render_template('index.html', lista_membros = lista_membros)
app.run()