import bcchapi
from decimal import Decimal
from datetime import datetime, timedelta

def get_clp_to_usd():
    # Inicializar bcchapi con tus credenciales de Bancocentra
    siete = bcchapi.Siete("na.xo3213@gmail.com", "Caquita11.")

    # Obtener la fecha y hora actual
    hoy = datetime.now()

    if hoy.weekday() == 5:  # sábado
        hoy -= timedelta(days=1)
    elif hoy.weekday() == 6:  # domingo
        hoy -= timedelta(days=2)

    # Convertir la fecha a formato YYYY-MM-DD
    hoy = hoy.strftime('%Y-%m-%d')

    try:
        # Obtener el tipo de cambio del viernes anterior de CLP a USD
        serie = siete.get("F073.TCO.PRE.Z.D", hoy, hoy)
        clp_to_usd = Decimal(serie.Series['Obs'][0]['value'])
        return clp_to_usd
    except Exception as e:
        print(f"Error al obtener el tipo de cambio: {e}")
        return None

def clp_to_usd_conversion(clp_amount):
    clp_to_usd = get_clp_to_usd()
    if clp_to_usd:
        usd_amount = clp_amount / clp_to_usd
        return usd_amount
    else:
        return None
    
def usd_to_clp_conversion(usd_amount):
    clp_to_usd = get_clp_to_usd()
    if clp_to_usd:
        clp_amount = usd_amount * clp_to_usd 
        clp_amount_int = int(clp_amount)
        return clp_amount_int
    else:
        return None
