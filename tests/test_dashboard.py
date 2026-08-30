from pages.dashboard import Dashboard

def test_ticket_create(authenticated_driver):

    # Ticket Create sayfasına giriş
    dashboard = Dashboard(authenticated_driver)
    dashboard.ticket_page()
    dashboard.ticket_create_button()
    dashboard.fill_firstname("8888")
    dashboard.search_customer()
    dashboard.find_customer("8888")
    print("Create ticket sayfasına gelmiştir.")

    # Ticket Create işlemi
    dashboard.fill_channel("Channel en")
    dashboard.fill_ticket_type("ayltest")
    dashboard.fill_category("Category e")
    dashboard.fill_sub_category("bcategories")
    dashboard.fill_priority("Low")
    dashboard.description("Test açıklamasıdır.")
    dashboard.create_ticket()
    print("işlem tamamlandı, ticket create başarılı...")

    is_redirected = dashboard.wait_for_url_contains("tickets")
    assert is_redirected, f"Kayıt sonrası yönlendirme başarısız! Mevcut URL: {authenticated_driver.current_url}"
    print("İşlem başarılı, sistem yeni biletin sayfasına sorunsuzca yönlendirildi.")