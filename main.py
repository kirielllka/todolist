<form method="POST", action="{%url 'todo-logout'%}">
    {% if user.is_authenticated%}
    {% csrf_token %}
        <button type="submit">Log out</button>
    {% else %}
    <a href="{% url 'todo-signup'%}"><h3>Sign-up</h3></a>
    <a href="{% url 'todo-login' %}"><h3>Log in</h3></a>
    {%endif%}

    </form>
    {%block content%}{%endblock%}

<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler"
                data-bs-target="#navbarNav" data-bs-toggle="collapse" type="button">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <form action="{%url 'todo-logout'%}" method="POST">
                    {% if user.is_authenticated%}
                    {% csrf_token %}
                    <li class="nav-item">
                        <a aria-current="page" class="nav-link active" href="#">
                            <button type="submit">Log out</button>
                        </a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'todo-signup'%}">Sign up</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'todo-login' %}">Log in</a>
                    </li>
                    {%endif%}
                </form>
            </ul>
        </div>
    </div>
</nav>
{%block content%}{%endblock%}
