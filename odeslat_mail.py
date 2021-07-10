#!/usr/bin/python
# coding=UTF-8

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import SQLConnect


def odeslat_mail(id_zamestnanec, testemail=True):
    sqlquery = "SELECT jmeno || prijmeni, email_pracovni from zamestnanec WHERE id_zamestnanec = %s" % id_zamestnanec
    zam = SQLConnect.query("SELECT", sqlquery)
    zam_jmeno = zam[0][0]
    zam_email = zam[0][1]
    body = """
    Dobrý den vážený kolego,
    
    V příloze zasílám novou verzi úvazků.
    
    S pozdravem a přáním pěkného dne
    Tajemník ústavu
    
    ----------------
    (Pokud Vám došel tento email stala se někde chyba. Email, prosím, ignorujte. Omlouvám se a přeji pěkný den. )
    """

    sender_email = "fake.tajemnik3@seznam.cz"
    testemail = True
    if testemail:
        receiver_email = 'fake.tajemnik3@seznam.cz'
    else:
        receiver_email = zam_email

    subject = "Nová verze úvazků"
    file_cesta = "C:\\Projects\\Tajemnik\\uvazky\\"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = 'UvazekZamestnanecID'+str(id_zamestnanec)+'.xlsx'
    # filename = 'test.xlsx'
    with open(file_cesta + filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    #
    # # Add attachment to message and convert message to string
    # message.attach(part)
    # if stav == 2:
    #     filename = idu + ".xlsx"  # In same directory as script
    #
    #     # Open PDF file in binary mode
    #     try:
    #         with open(file_cesta_2 + filename, "rb") as attachment:
    #             # Add file as application/octet-stream
    #             # Email client can usually download this automatically as attachment
    #             part = MIMEBase("application", "octet-stream")
    #             part.set_payload(attachment.read())
    #         encoders.encode_base64(part)
    #
    #         # Add header as key/value pair to attachment part
    #         part.add_header(
    #             "Content-Disposition",
    #             f"attachment; filename= {filename}",
    #         )
    #
    #         # Add attachment to message and convert message to string
    #         message.attach(part)
    #
    #     except:
    #         print("Firma: %s, nenalezen podrobný výpis, odesílám obecný výpis" % firma)
    #     # Encode file in ASCII characters to send by email

    text = message.as_string()
    with smtplib.SMTP_SSL("smtp.seznam.cz", 465) as server:
        server.ehlo()
        server.login('fake.tajemnik3@seznam.cz', 'heslo1234')
        server.sendmail(sender_email, receiver_email, text)
