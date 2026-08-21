from billing_controller import record_successful_payment, fetch_all_active_nodes

def run_test():
    print("Simulating incoming Stripe webhook event...")
    
    # Simulate a successful payment payload from a B2B client
    test_company = "Apex Autonomous Corp"
    test_email = "billing@apexautonomous.io"
    test_retainer = 1500.00
    
    # Record the payment via the billing controller
    record_successful_payment(test_company, test_email, test_retainer)
    
    # Fetch and display all active retainer nodes
    print("\nQuerying active database nodes:")
    active_nodes = fetch_all_active_nodes()
    for node in active_nodes:
        print(f"Node ID: {node[0]} | Company: {node[1]} | Email: {node[2]} | Status: {node[3]} | Retainer: ${node[4]}")

if __name__ == '__main__':
    run_test()
