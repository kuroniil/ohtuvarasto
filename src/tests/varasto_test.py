import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 9)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_ei_voida_laittaa_liikaa(self):
        tilavuus = self.varasto.tilavuus
        
        self.varasto.lisaa_varastoon(tilavuus + 1)

        self.assertAlmostEqual(tilavuus, self.varasto.tilavuus)

    def test_varastosta_ei_voida_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        otettu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(otettu_maara, 5)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ei_voida_luoda_virheellista_varastoa(self):
        # Vääränlainen tilavuus ja saldo
        virheellinen_varasto = Varasto(-10, -10)
        
        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)

    def test_uudessa_varastossa_ei_voi_olla_enemman_saldoa_kun_tilaa(self):
        varasto = Varasto(10, 11)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_varastoon_ei_lisata_negatiivista_maaraa(self):
        alku_saldo = self.varasto.saldo
        
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(alku_saldo, self.varasto.saldo)

    def test_varastosta_ei_oteta_negatiivista_maaraa(self):
        alku_saldo = self.varasto.saldo
        
        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(alku_saldo, self.varasto.saldo)

    def test_varasto_tulostuu_oikein(self):
        oikea_tuloste = "saldo = 0, vielä tilaa 10"

        self.assertEqual(oikea_tuloste, str(self.varasto))