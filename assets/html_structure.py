def get_angebot_template():
    """
    Retrieves the html structure for formatting the offer.
    """

    template = """<!DOCTYPE html>
    <html lang="de">
    <head>
    <meta charset="UTF-8">
    <style>
    @page {
    size: A4;
    margin: 30mm 20mm 30mm 20mm;
    font-size: 8px;
    font-family: Helvetica, sans-serif; 

    @bottom {
        content: "";
        border-top: 1px solid #ccc;
        height: 1px;
        margin-top: 2mm;
    }

    @bottom-left {
        content: "────────────────────────────────────────────" "\A"
                "GastroTech Solutions" "\A"
                "Kaiserstrasse 78" "\A"
                "42477 Radevorwald" "\A"
                "Deutschland";
        white-space: pre;
    }

    @bottom-center {
        content: "──────────────────────────────────────────────" "\A" 
                "Geschäftsführung Aravinthan Kanesarasa" "\A"
                "Tel. 017621632965" "\A"
                "E-Mail aravinthan601@hotmail.com" "\A"
                "\A";
        white-space: pre;
    }

    @bottom-right {
        content: "────────────────────────────────────────────" "\A"
                "Bank Qonto" "\A"
                "IBAN DE96 1001 0123 4600 4381 86" "\A"
                "Steuer-Nr. 33458604806" "\A"
                "\A";
        white-space: pre;
    }
    }
    html {
    font-size: 8px;
    line-height: 1.5;
    }

    body {
        font-family: Helvetica, sans-serif;
        margin: 0;
        padding: 0;
        color: #222;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin: 30px 0px 0 0px;
    }

    .customer-info {
        max-width: 65%;
    }

    .logo {
        width: 130px;
        height: auto;
    }
    .logo img {
        width: 100%;
        height: auto;
    }

    /* Struktur */
    h2 {
        margin: 30px 30px 5px 30px;
        font-size: 11px;
    }
    p, th {
        font-size: 9px;
        margin: 0 30px;
    }

    table.content-table td {
        margin: 0 30px;
    }

    td {
        font-size: 9px;
        margin: 0; /* Kein globales margin mehr auf <td>! */
    }
    table {
        border-collapse: separate;
        border-spacing: 0 5px;
        margin: 18px 0px 0 0px;
        width: 100%;
    }
    th {
        background-color: #f0f0f0;
        text-align: left;
        padding: 4px;
        border-bottom: 1px solid #ccc;
    }
    td {
        background-color: #ffffff;
        padding: 4px;
        vertical-align: top;
        border: 1px solid #e0e0e0;
        border-top: none;
    }
    tr.no-split {
        page-break-inside: avoid;
    }
    .product-img {
        display: block;              /* Makes margin auto work */
        margin: 0 auto;              /* Center horizontally */
        max-width: 100%;
        max-height: 3.5cm;             /* or another fixed value */
        height: auto;
        object-fit: contain;
    }
    .totals-box {
        margin: 35px 30px 0 auto;
        width: 40%;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 8px 10px;
        font-size: 9px;
        background-color: #f9f9f9;
        page-break-inside: avoid;
    }
    .totals-box .row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 4px;
    }
    .totals-box .row.total {
        font-weight: bold;
        border-top: 1px solid #ccc;
        padding-top: 4px;
        margin-top: 6px;
    }

    td.product-description {
    padding: 2px 4px;
    line-height: 1.3;
    }

    .product-title {
    font-weight: bold;
    font-size: 9px;
    margin: 0;
    padding: 0;
    line-height: 1.2;
    }
    .product-alternative {
    font-weight: bold;
    font-size: 10px;
    line-height: 1.2;
    color: #B22222;
    }

    .product-text {
    font-size: 9px;
    margin: 0;
    padding: 0;
    line-height: 1.3;
    white-space: pre-wrap;
    }


    /* Customer block */
    .customer-block {
        font-size: 9px;            /* Make it bigger */
        line-height: 1.2;           /* Improve readability */
        margin-left: 0px;          /* Align exactly with table */
        margin-right: 15px;
        margin-bottom: 15px;
    }

    .customer-block p {
        font-size: 9px;
        line-height: 1.3;
        margin: 0;
    }

    /* Customer block 2 */
    .customer-block-2 {
        font-size: 9px;
        line-height: 1.2;
        margin-left: 40px;
        margin-right: 0px;
        margin-bottom: 15px;
    }
    
    .customer-block-2 p {
        font-size: 9px;
        line-height: 1.3;
        margin: 0;
    }

    .anschreiben {
        line-height: 1.6;
    }

    .anschreiben p {
        font-size: 9px;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        text-indent: 0;
    }

    .angebot-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0;
        padding: 0;
        text-indent: 0;
    }

    .angebot-title {
        font-size: 16px;
        font-weight: bold;
    }

    .angebot-datum {
        font-size: 11px;
        color: #444;
    }

    /* Restlicher Text */
    .hinweise-block {
        font-size: 10px;
        margin-left: 0;
        line-height: 1.6;
    }

    .hinweise-block ol {
        font-size: 9px;
        padding-left: 2;
    }

    .hinweise-block li {
        font-size: 9px;
        margin-bottom: 4px;
        padding-left: 14px;
    }
    .AGB {
        font-size: 9px;
        margin-right: 0px;
        margin-bottom: 10px;
    }

    .AGB p {
        font-size: 9px;
        margin: 0 30px;
        margin-bottom: 10px;
        text-align: justify;
    }

    .agb-text {
        margin-top: 4px;
    }

    .unterschrift {
        margin-top: 15mm;
        text-align: right;
        font-size: 9px;
    }

    .unterschrift .line {
        border-top: 1px solid #000;
        width: 200px;
        margin-bottom: 2mm;
        float: right;
    }

    .unterschrift {
        margin-top: 15mm;
        font-size: 9px;
        text-align: right;
    }

    .line-with-label {
        display: inline-block;
        text-align: center;
    }

    .line {
        border-top: 1px solid #000;
        width: 200px;
        margin: 0 auto 2mm auto;
    }

    .label {
        width: 200px;
        text-align: center;
    }

    /* Footer wird durch diese Box "nach unten gedrückt" */
    .footer-push {
        height: 100px;
    }
    </style>
    </head>
    <body>

    <p style="font-size: 7px; margin: 0;">GastroTech Solutions - Kaiserstrasse 78 - 42477 Radevorwald</p>

    <div class="header">
    <div class="customer-block">
        <p style="font-size: 13px;"><strong>{{ kunde['Firma'] }}</strong></p>
        <p>{{ kunde['Anrede'] }} {{ kunde['Vorname'] }} {{ kunde['Nachname'] }}</p>
        <p>{{ kunde['Adresse'] }}</p>
        <p>{{ kunde['PLZ'] }} {{ kunde['Ort'] }}</p>
        <p>Tel.: {{ kunde['Telefonnummer'] }}</p>
        <p>E-Mail: {{ kunde['E_Mail'] }}</p>
    </div>

    <div class="customer-block-2">
        <p style="font-size: 13px;"><strong>Angebots-Nummer {{ angebot_id }}</strong></p>
        <p>Datum: {{ aktuelles_datum }}</p>
        <p>Kunden-Nr.: {{ kunde['Kunden_Nummer'] }}</p>
        <p>Ihr Ansprechpartner: {{ kunde['Ansprech_Partner'] }}</p>
        <p>E-Mail: {{ kunde['Ansprech_Partner_Email'] }}</p>
    </div>
    <div class="logo">
        <img src="{{ logo_base64 }}" alt="Logo">
    </div>
    </div>

    <p style="margin-top: 20px;"></p>
    
    <div class="angebot-row">
    <div class="angebot-title" style="font-size: 13px;">Angebot: {{ angebot_id }}</div>
    </div>

    <div class="anschreiben">
    {% if kunde['Anrede'] == 'Herr' %}
    <p>Sehr geehrter Herr {{ kunde['Nachname'] }},</p>
    {% elif kunde['Anrede'] == 'Frau' %}
    <p>Sehr geehrte Frau {{ kunde['Nachname'] }},</p>
    {% else %}
    <p>Sehr geehrte Damen und Herren,</p>
    {% endif %}
    <p>vielen Dank für Ihre Anfrage. Gerne unterbreiten wir Ihnen das gewünschte freibleibende Angebot.</p> 

    <p>Für Rückfragen stehen wir Ihnen jederzeit gerne zur Verfügung.</p>
    <p>Wir bedanken uns sehr für Ihr Vertrauen.</p>
    </div>
    <table>
    <colgroup>
        <col style="width: 5%;">
        <col style="width: 55%;">
        <col style="width: 8%;">
        <col style="width: 15%;">
        <col style="width: 15%;">
    </colgroup>
    <thead>
    <tr>
    <th>Pos.</th>
    <th>Beschreibung</th>
    <th>Menge</th>
    <th>Einzelpreis</th>
    <th>Gesamtpreis</th>
    </tr>
    </thead>
    <tbody>
    {% for row in products %}
    <tr class="product-row{% if loop.index > 1 %} no-split{% endif %}">
    <td><strong>{{ row['Positionsbezeichnung'] }}</strong></td>
    <td class="product-description">
    {% if row['Alternative'] == True %}
        <div class="product-alternative">Alternativ-Option</div>
    {% endif %}
    {% if row['Titel'] %}
        <div class="product-title">{{ row['Titel'] }}</div>
    {% endif %}
    <div class="product-text">{{ row['Beschreibung'] or ''}}</div>
    </td>
    <td>
    {% if not row.Alternative and row.Menge is not none %}
        {% if row.Menge == row.Menge|int %}
            {{ row.Menge|int }}
        {% else %}
            {% set formatted = "%.2f"|format(row.Menge) %}
            {{ formatted.replace('.', ',') }}
        {% endif %}
    {% endif %}
    </td>
    <td>{{ row.Preis | german_currency }} EUR</td>
    <td>
    {% if not row.Alternative %}
        {% if row.Menge is not none %}
        {{ row.Gesamtpreis | german_currency }} EUR
        {% else %}
        {{ row.Preis | german_currency }} EUR
        {% endif %}
    {% endif %}
    {% endfor %}
    </tbody>
    </table>

    <div class="totals-box">
    <div class="row">
        <div>Netto Gesamt:</div>
        <div>{{ netto | german_currency }} EUR</div>
    </div>

    {% if rabatt != 0 %}
    <div class="row">
        <div>{{ rabatt|replace('.', ',') }}% Rabatt:</div>
        <div>-{{ rabatt_num | german_currency }} EUR</div>
    </div>
    {% endif %}

    {% if if_mwst == True %}
    <div class="row">
        <div>19% MwSt:</div>
        <div>{{ mwst | german_currency }} EUR</div>
    </div>
    {% endif %}

    {% if if_mwst == False %}
    <div class="row">
        <div>ATU-Nummer:</div>
        <div>{{atu}}</div>
    </div>
    {% endif %}

    <div class="row total">
        <div>Brutto Gesamt:</div>
        <div>{{ brutto | german_currency }} EUR</div>
    </div>
    </div>
    </div>
    </body>
    </html>"""
    return template