# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    import os

    import matplotlib.pyplot as plt
    import pandas as pd

    os.makedirs("docs", exist_ok=True)

    def load_data():
        return pd.read_csv("files/input/shipping-data.csv")

    def create_visual_for_shipping_per_warehouse(df):
        plt.figure()

        counts = df["Warehouse_block"].value_counts()

        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )

        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.savefig("docs/shipping_per_warehouse.png")
        plt.close()

    def create_visual_for_shipment(df):
        plt.figure()

        counts = df["Mode_of_Shipment"].value_counts()

        counts.plot.pie(
            title="Mode of Shipment",
            ylabel="",
            wedgeprops={"width": 0.35},
            colors=["tab:blue", "tab:orange", "tab:green"],
        )

        plt.savefig("docs/mode_of_shipment.png")
        plt.close()

    def create_visual_for_average_customer_rating(df):
        plt.figure()

        ratings = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )

        ratings.columns = ratings.columns.droplevel()

        ratings = ratings[["mean", "min", "max"]]

        plt.barh(
            y=ratings.index,
            width=ratings["max"] - 1,
            left=ratings["min"],
            height=0.9,
            color="lightgray",
        )

        colors = [
            "tab:green" if value >= 3 else "tab:orange"
            for value in ratings["mean"]
        ]

        plt.barh(
            y=ratings.index,
            width=ratings["mean"] - 1,
            left=ratings["min"],
            height=0.5,
            color=colors,
        )

        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")

        plt.savefig("docs/average_customer_rating.png")
        plt.close()

    def create_visual_for_weight_distribution(df):
        plt.figure()

        df["Weight_in_gms"].plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )

        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.savefig("docs/weight_distribution.png")
        plt.close()

    df = load_data()

    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.write(
            """<!DOCTYPE html>
<html>
<head>
    <title>Shipping Dashboard</title>
</head>
<body>
    <h1>Shipping Dashboard</h1>

    <div style="width:45%; float:left;">
        <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse" width="100%">
        <img src="mode_of_shipment.png" alt="Mode of Shipment" width="100%">
    </div>

    <div style="width:45%; float:left;">
        <img src="average_customer_rating.png" alt="Average Customer Rating" width="100%">
        <img src="weight_distribution.png" alt="Weight Distribution" width="100%">
    </div>

</body>
</html>"""
        )


if __name__ == "__main__":
    pregunta_01()
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
