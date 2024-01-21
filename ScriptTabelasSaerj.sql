USE [SAERJ]
GO

/****** Object:  Table [dbo].[Perfis]    Script Date: 16/1/2024 18:05:50 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Perfis](
	[CodPerfil] [smallint] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[DescPerfil] [varchar](50) NULL,
	[PerfilAdministrador] [char](1) NULL,
	[DataAtualizacao] [datetime] NULL,
 CONSTRAINT [PK_Perfis] PRIMARY KEY CLUSTERED 
(
	[CodPerfil] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 90) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


USE [SAERJ]
GO

/****** Object:  Table [dbo].[Usuarios]    Script Date: 16/1/2024 18:06:43 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Usuarios](
	[Numero] [smallint] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[Iniciais] [varchar](10) NOT NULL,
	[CodPerfil] [smallint] NOT NULL,
	[Nome] [varchar](100) NULL,
	[Email] [varchar](100) NULL,
	[Status] [char](1) NULL,
	[Senha] [varbinary](100) NULL,
	[IdRecuperaSenha] [varchar](20) NULL,
	[ResetouSenha] [char](1) NULL,
 CONSTRAINT [PK_Usuarios] PRIMARY KEY CLUSTERED 
(
	[Numero] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 90) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


USE [SAERJ]
GO

/****** Object:  Table [dbo].[Transacoes]    Script Date: 16/1/2024 18:07:04 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Transacoes](
	[CodTransacao] [smallint] IDENTITY(1,1) NOT NULL,
	[DescTransacao] [varchar](100) NULL,
	[TipoTransacao] [varchar](25) NULL,
	[DataAtualizacao] [datetime] NULL,
 CONSTRAINT [PK_Transacoes] PRIMARY KEY CLUSTERED 
(
	[CodTransacao] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 90) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO



USE [SAERJ]
GO

/****** Object:  Table [dbo].[Acessos]    Script Date: 16/1/2024 18:05:35 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Acessos](
	[CodPerfil] [smallint] NOT NULL,
	[CodTransacao] [smallint] NOT NULL,
	[Inclui] [char](1) NULL,
	[Altera] [char](1) NULL,
	[Exclui] [char](1) NULL,
	[Executa] [char](1) NULL,
 CONSTRAINT [PK_Acessos] PRIMARY KEY CLUSTERED 
(
	[CodPerfil] ASC,
	[CodTransacao] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 90) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO
