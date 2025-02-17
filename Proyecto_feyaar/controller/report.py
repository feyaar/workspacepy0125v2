from config.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    query = """
        SELECT 
            r.nombre AS region,
            p.pais,
            v.product_id,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE pc ON v.postal_code = pc.code
        JOIN 
            PAIS p ON pc.pais = p.name
        JOIN 
            REGION r ON p.id = r.pais_id
        GROUP BY 
            r.nombre, p.pais, v.product_id
        ORDER BY 
            total_vendido DESC;
    """
    df = pd.read_sql_query(query, conn)
    fecha = "08-02"
    path = f"/workspaces/workspacepy0125v2/Proyecto_feyaar/files/data-{fecha}.csv"
    df.to_csv(path)
    sendMail(app, path)

def sendMail(app: App, data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com', 'Reporte de Ventas', 'Adjunto el reporte de ventas y regiones actualizado.', data)
