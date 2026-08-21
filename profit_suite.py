import stripe
from flask import Flask, jsonify, request

app = Flask(__name__)

# Key Zero Protocol: Local placeholder key until production activation
stripe.api_key = "sk_test_LOCAL_PLACEHOLDER_KEY"

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        tier_price_id = data.get('price_id', 'price_default_tier')
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': tier_price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://cryptogod256.github.io/Nexal-No-Hitch-Riches/?success=true',
            cancel_url='https://cryptogod256.github.io/Nexal-No-Hitch-Riches/?canceled=true',
        )
        return jsonify({'url': checkout_session.url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)
