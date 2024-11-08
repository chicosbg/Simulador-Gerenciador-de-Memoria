from rich.table import Table 
from rich.console import Console
import logging
from rich.logging import RichHandler

class LoggerUtils:
    def __init__(self) -> None:
        self.console = Console()
        logging.basicConfig(
            level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
        )
        self.log = logging.getLogger("rich")
        
    def table(self, title, rows, tam_memoria):
        table = Table(title=title, show_header=False)
        arg = []
        for row in range(0, tam_memoria):
            if(len(rows) > row): 
                arg.append(rows[row].__str__().replace("[", "").replace("]", ""))
                continue
            arg.append("")
                
        table.add_row(*arg)
        self.console.print(table)
        
    def info(self, mensagem):
        self.log.info(mensagem)
        
    def error(self, mensagem):
        self.log.error(mensagem)
    
    def warning(self, mensagem):
        self.log.warning(mensagem)