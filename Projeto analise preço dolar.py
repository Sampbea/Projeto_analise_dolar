import requests

def get_exchange_rate():
    try:
   
        response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json")
        data = response.json()


        if response.status_code == 200:

            exchange_rate = data[0]["valor"]
            return exchange_rate
        else:
            print("Falha ao obter a taxa de câmbio:", response.status_code)
            return None
    except Exception as e:
        print("Ocorreu um erro:", e)
        return None

def main():

    exchange_rate = get_exchange_rate()
    if exchange_rate is not None:
        print("Taxa de câmbio do dólar para o real brasileiro:", exchange_rate)
    else:
        print("Não foi possível obter a taxa de câmbio.")

if __name__ == "__main__":
    main()
