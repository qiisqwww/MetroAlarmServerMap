from src.entities import Line

__all__ = [
    "lines_list"
]


lines_list = [
    Line(
        id=1001,
        city_id=1,
        name="Сокольническая линия",
        alias="1 линия",
        logo_path="msk_1.png"
    ),
    Line(
        id=1002,
        city_id=1,
        name="Замоскворецкая линия",
        alias="2 линия",
        logo_path="msk_2.png"
    ),
    Line(
        id=2001,
        city_id=2,
        name="Кировско-Выборгская линия",
        alias="1 линия",
        logo_path="spb_1.png"
    ),
    Line(
        id=2002,
        city_id=2,
        name="Московско-Петроградская линия",
        alias="2 линия",
        logo_path="spb_2.png"
    )
]
