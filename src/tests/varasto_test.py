import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_negatiivisen_tilavuuden_luominen(self):
        negatiivinen = Varasto(-1)

        self.assertEqual(negatiivinen.tilavuus, 0)

    def test_negatiivisen_saldon_luominen(self):
        negatiivinen = Varasto(10, -1)

        self.assertEqual(negatiivinen.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivisen_summan_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liian_suuren_lisays(self):
        self.varasto.lisaa_varastoon(20)
        self.assertEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)


    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen(self):
        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertEqual(saatu_maara, 0)

    def test_liian_suuri_otto(self):
        self.varasto.lisaa_varastoon(10)

        saatu_maara = self.varasto.ota_varastosta(20)
        self.assertEqual(saatu_maara, self.varasto.tilavuus)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_funktion_testaus(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")