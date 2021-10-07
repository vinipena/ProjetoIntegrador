<!doctype html>
<html lang="pt-BR">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS  -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- CSS da Página-->
    <link rel="stylesheet" href="./style/style.css">
    <title>ItapeVagas</title>
</head>
  <body>
    <header> 
        <nav class="menu">
            <div id="mySidenav" class="sidenav">
                <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                <a href="#">Home</a>
                <a href="#">Candidatos</a>
                <a href="#">Empresas</a>
            </div>
            
            <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776;</span>
            <h1 >ItapeVagas</h1>
        </nav>
    </header>
    <div class="container">
        <section class="search-bar">
            <form class="formulario-busca">
                <input type="text" id="busca" class='barra-busca' name="busca" placeholder="Busque sua vaga!">
                <input type="submit" class=' botao-busca' value="Buscar Vaga">
            </form>
        </section>
        <section class='nosso-projeto'>Nosso Projeto</section>
        <section class= 'quem-somos'>Quem Somos</section>
    </div>
    <footer class= 'rodape'>
        Rodapé
    </footer>


    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script src="./scripts/scripts.js"></script>
</body>
</html>