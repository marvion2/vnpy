from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ib import IbGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_datamanager import DataManagerApp
from vnpy_spreadtrading import SpreadTradingApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_paperaccount import PaperAccountApp
from vnpy_chartwizard import ChartWizardApp
from vnpy_webtrader import WebTraderApp
from vnpy_riskmanager import RiskManagerApp
from vnpy_algotrading import AlgoTradingApp

from vnpy_xt import XtGateway

def main():
    """Start VeighNa Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(IbGateway)
    main_engine.add_gateway(XtGateway)

    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(DataManagerApp)
    main_engine.add_app(SpreadTradingApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(ChartWizardApp)
    # main_engine.add_app(PaperAccountApp)
    main_engine.add_app(WebTraderApp)
    main_engine.add_app(RiskManagerApp)
    main_engine.add_app(AlgoTradingApp)


    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
